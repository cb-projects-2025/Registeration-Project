import pytest
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Utilities.Functions import *



class Xpert():

    def __init__(self, driver):
        self.driver = driver

    def Xpertbottesting(self,username,password,institution,degree,name,startyear,endyear,description,jobseeker):
        Xpertbbotlogin(self,username,password,institution,degree,name,startyear,endyear,description,jobseeker)

    def XpertSign(self,username,password,confirmpass,email):
        Signup(self,username,password,confirmpass,email)