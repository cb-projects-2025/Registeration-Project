import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Set wide layout
st.set_page_config(layout="wide", page_title="User Registration Summary")

# Custom title with styling
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #3366cc;
            margin-bottom: 30px;
        }
    </style>
    <div class="main-title">📊 User Registration Summary</div>
    """,
    unsafe_allow_html=True
)

# Database connection
db_path = r"C:\Users\Charbel\Desktop\Data Science X5\Registration App.db"
conn = sqlite3.connect(db_path)

# Load views
views = ['USER_DEMOGRAPHICS', 'USERS_PER_BATCH', 'PAYMENT_V']
USER_DEMOGRAPHICS = pd.read_sql_query(f"SELECT * FROM {views[0]}", conn)
USERS_PER_BATCH = pd.read_sql_query(f"SELECT * FROM {views[1]}", conn)
PAYMENT_V = pd.read_sql_query(f"SELECT * FROM {views[2]}", conn)

conn.close()

# Clean column names
USER_DEMOGRAPHICS.columns = USER_DEMOGRAPHICS.columns.str.strip()
USERS_PER_BATCH.columns = USERS_PER_BATCH.columns.str.strip()
PAYMENT_V.columns = PAYMENT_V.columns.str.strip()

# === Top-level Metrics ===
st.markdown("### 👥 Demographics & Top Institutions")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("**Gender Distribution**")
    fig_gender = px.pie(USER_DEMOGRAPHICS, names='GENDER', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    st.markdown("**Age Group**")
    fig_age = px.pie(USER_DEMOGRAPHICS, names='AGE_GROUP_BUCKET', hole=0.4, color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_age, use_container_width=True)

with col3:
    st.markdown("**Academic Level**")
    fig_academic = px.pie(USER_DEMOGRAPHICS, names='ACADEMIC_LEVEL', hole=0.4, color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_academic, use_container_width=True)

with col4:
    st.markdown("**Top 10 Institutions**")
    top_institutions = USER_DEMOGRAPHICS['INSTITUTION_NAME'].value_counts().nlargest(10).reset_index()
    top_institutions.columns = ['INSTITUTION_NAME', 'USER_COUNT']
    fig_institution_bar = px.bar(
        top_institutions,
        x='USER_COUNT',
        y='INSTITUTION_NAME',
        orientation='h',
        labels={'INSTITUTION_NAME': 'Institution', 'USER_COUNT': 'Number of Users'},
        color='USER_COUNT',
        color_continuous_scale='Blues',
        text_auto=True  # Display number inside the bar
    )
    fig_institution_bar.update_layout(showlegend=False, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_institution_bar, use_container_width=True)

# === Batch Metrics ===
st.markdown("---")
st.markdown("### 📦 Batches Overview")
col_batch, col_payment = st.columns(2)

with col_batch:
    st.markdown("**Users per Batch**")
    fig_batch = px.bar(
        USERS_PER_BATCH,
        x="No. of Users",
        y="BATCH",
        orientation="h",
        color="No. of Users",
        color_continuous_scale="viridis",
        labels={"BATCH": "Batch Name", "No. of Users": "Number of Users"},
        text_auto=True  # Display number inside the bar
    )
    fig_batch.update_layout(showlegend=False, yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_batch, use_container_width=True)

with col_payment:
    st.markdown("**Total Payments per Batch**")
    fig_payment = px.bar(
        PAYMENT_V,
        x="AMOUNT",
        y="BATCH",
        orientation="h",
        color="AMOUNT",
        color_continuous_scale="sunset",
        labels={"BATCH": "Batch Name", "AMOUNT": "Total Payment ($)"},
        text_auto=True  # Display number inside the bar
    )
    
    # Adjust to show full payment amount without the 'K' abbreviation
    fig_payment.update_layout(showlegend=False, yaxis=dict(autorange="reversed"))
    
    # Add formatting to show full amount (no 'K')
    fig_payment.for_each_trace(lambda t: t.update(texttemplate='%{x:,.0f}'))  # Format numbers without abbreviation
    
    st.plotly_chart(fig_payment, use_container_width=True)

# === Optional footer ===
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>© 2025 Data Science X5 - Dashboard powered by Streamlit</div>",
    unsafe_allow_html=True
)
