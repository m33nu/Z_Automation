from selenium import webdriver
import os
import slack
import time
import pandas as pd
import ssl as ssl_lib
import certifi
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def addnewmail(driver, email):
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "buttonAddNewEmail")))
    driver.find_element_by_id("buttonAddNewEmail").click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "general-generalSection-name")))
    driver.find_element_by_id("general-generalSection-name").send_keys(email)
    driver.find_element_by_id("general-generalSection-loginAsUser").click()
    driver.find_element_by_id("general-generalSection-password").send_keys("password@123")
    driver.find_element_by_id("general-generalSection-passwordConfirmation").send_keys("password@123")
    driver.find_element_by_id("general-generalSection-mboxQuotaValue-specific").click()
    driver.find_element_by_id("general-generalSection-mboxQuotaValue-specific-input").send_keys(1)
    driver.find_element_by_id("btn-send").click()
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "buttonAddNewEmail")))
	

def readexcel():
    pd.read_excel
    filename = "data.xlsx"
    df = pd.read_excel(filename,'Names',usecols = "A")
    return df.values

def main():	
    driver = webdriver.Chrome("drivers/chromedriver.exe")
    driver.get("url")
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    client = slack.WebClient(token=os.environ['SLACK_ZYLLU_API_TOKEN'],ssl=ssl_context)
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "loginSection-username")))
    driver.find_element_by_id("loginSection-username").send_keys("username")
    driver.find_element_by_id("loginSection-password").send_keys("password")
    driver.find_element_by_name("send").click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT, "taknator.com")))
    driver.find_element_by_link_text("taknator.com").click()
    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT, "Email Addresses")))
    driver.find_element_by_link_text("Email Addresses").click()
    list = readexcel()
    for i in range (38,79):
        email = list[i][0]
        print(email + 'Index = '.format(i))
        addnewmail(driver, email)
        message = email + "@taknator.com"
        response = client.chat_postMessage(channel='#taknator-emails',text=message)        	        
        i = i+1
if __name__ == '__main__':
    main()