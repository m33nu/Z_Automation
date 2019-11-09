from selenium import webdriver
import os
import slack
import time
import pandas as pd
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from random import seed
from random import randint
import sys


def main():
	driver = webdriver.Chrome("drivers/chromedriver.exe")
	driver.get("url")
	emailaddress = sys.argv[1] if len(sys.argv) > 1 else driver.close()
	chrome_options = Options()
	chrome_options.add_experimental_option("detach", True)
	time.sleep(6)
	seed(0)
	allCategories = driver.find_elements_by_xpath(
	    "//div[@id='vote']//div[@class='Vote-categories']/div")
    # print( 'allCategories' + allCategories)
	print('allCategories count =' + str(len(allCategories)))
	for index, eachCategory in enumerate(allCategories, start=0):
	    categoryHeading = eachCategory.find_element_by_xpath(
	        "./div[@class='Vote-category-heading']").text
	    print('categoryHeading =' + categoryHeading)
	    nomineeList = eachCategory.find_elements_by_xpath(
	        "./div[@class='Vote-nominees']/div")
	    print('nomineeList count =' + str(len(nomineeList)))
	    # print( 'nomineeList' + nomineeList)
	    if categoryHeading == "Startup of the Year":
	        for eachNominee in nomineeList:                
	            companyName = eachNominee.find_element_by_xpath(
                    "./div[@class='Vote-nominee-text']/a").text
	            print('companyName =' + companyName)
	            ourName = "Tachyon Systems Pty Ltd"
	            if companyName.lower() == ourName.lower():
	                eachNominee.find_element_by_xpath(
                        "./button[@class='Vote-nominee']").click()
	    else:
	        max = len(nomineeList)
	        print("max =", max-1)
	        randomIndex = randint(0, max-1)
	        print('Random Index =', randomIndex)
	        nomineeList[randomIndex].find_element_by_xpath(
                "./button[@class='Vote-nominee']").click()
	emailField = driver.find_element_by_xpath ("//input[@class='Vote-signup-input']").send_keys(emailaddress) 
	print( 'Done')
	time.sleep(3000)
	
if __name__ == '__main__':
    main()
