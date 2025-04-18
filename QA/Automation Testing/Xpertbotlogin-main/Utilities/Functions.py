#All the fucntions we need to run 
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from Utilities.utils import AutomationLogger
from pages.creds import *



def Xpertbbotlogin(self,username,password,institution,degree,name,startyear,endyear,description,jobseeker):
    log=AutomationLogger.automation()
    email_locator= (By.XPATH,email)
    log.info("Location email")
    try:
        WebDriverWait(self.driver,60).until(
            EC.presence_of_element_located(email_locator)
        )
    except NoSuchElementException as e:
        self.log.warning("unable to locate element")
    self.driver.find_element(By.XPATH,email).clear() 
    time.sleep(1)
    self.driver.find_element(By.XPATH,email).send_keys(username)
    log.info("Sent username")
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="password"]').clear() 
    self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(1)
    self.driver.find_element(By.XPATH,'/html/body/div/div/form/button').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[1]/ul[1]/li[1]/a').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/a').click()
    time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="institution"]').send_keys(institution)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(institution)
    #time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="degree"]').send_keys(degree)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(degree)
    #time.sleep(1)
    self.driver.find_element(By.XPATH,'//*[@id="name"]').send_keys(name)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(name)
    #time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="start_year"]').send_keys(startyear)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(startyear)
    #time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="end_year"]').send_keys(endyear)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(endyear)
    #time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="description"]').send_keys(description)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(description)
    #time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[2]/div[2]/form/div[1]/div/div[7]/div[2]/div[1]/select').send_keys(jobseeker)
    time.sleep(1)
    #self.driver.find_element(By.XPATH,email).send_keys(jobseeker)
    #time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[2]/div[2]/form/div[2]/button[2]/span').click()
    time.sleep(1) 
    self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[1]/div[2]/div/button/div').click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT,'Logout').click()
    time.sleep(3)

def Signup(self):
        log=AutomationLogger.automation()
        email_locator= (By.XPATH,email)
        log.info("Location email")
        try:
            WebDriverWait(self.driver,60).until(
                EC.presence_of_element_located(email_locator)
            )
        except NoSuchElementException as e:
            self.log.warning("unable to locate element")
        self.driver.find_element(By.XPATH,email).send_keys(username)
        log.info("Sent username")
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div/div/form/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="nova"]/div/div[2]/div[1]/div[2]/div/button/div').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT,'Logout').click()
        time.sleep(3)