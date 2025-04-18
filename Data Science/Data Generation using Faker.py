import pandas as pd
import random
from faker import Faker
import os

# Setup Faker and seed
fake = Faker('en_US')
Faker.seed(0)
random.seed(0)

# Lebanese prefixes
lebanese_prefixes = ['71', '76', '03']

# Ensure only one admin
admin_assigned = False

def generate_user(id):
    global admin_assigned
    gender = random.choice(["Male", "Female"])
    first_name = fake.first_name_male() if gender == "Male" else fake.first_name_female()
    last_name = fake.last_name()
    email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
    password = fake.password(length=10)
    phone_number = f"+961{random.choice(lebanese_prefixes)}{random.randint(1000000, 9999999)}"
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=40).strftime('%Y-%m-%d')
    role = "Admin" if not admin_assigned else "User"
    if not admin_assigned:
        admin_assigned = True
    status = random.choice(["Active", "Inactive"])
    has_paid = random.choice([0, 1])
    created_at = fake.date_time_between(start_date='-3M', end_date='now')
    updated_at = fake.date_time_between(start_date=created_at, end_date='now')
    
    return {
        "ID": id,
        "FIRST_NAME": first_name,
        "LAST_NAME": last_name,
        "EMAIL": email,
        "PASSWORD": password,
        "PHONE_NUMBER": phone_number,
        "DATE_OF_BIRTH": date_of_birth,
        "GENDER": gender,
        "ROLE": role,
        "STATUS": status,
        "HAS_PAID": has_paid,
        "CREATED_AT": created_at.strftime('%Y-%m-%d %H:%M'),
        "UPDATED_AT": updated_at.strftime('%Y-%m-%d %H:%M')
    }

# Generate 500 users
users_data = [generate_user(i+1) for i in range(500)]

# Convert to DataFrame
users_df = pd.DataFrame(users_data)

# Define file path for desktop
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "random_users.xlsx")

# Export DataFrame to Excel
users_df.to_excel(file_path, index=False)

print(f"Data successfully exported to {file_path}")
