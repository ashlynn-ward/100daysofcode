#Downloading Population Tables
#Ashlynn Ward, June 30, 2025
#This program uses Selenium webdriver to scrape population data from Statistics Canada's website. It then saves it into a CSV, and also 
#downloads the information from the site. The purpose of this program is to practice accessing and interacting with webdrivers. 

#Import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas
import ssl
import io

# Temporarily disable SSL verification to use pandas to read html - this method is not intended for projects in production
ssl._create_default_https_context = ssl._create_unverified_context

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create driver
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www150.statcan.gc.ca/n1/en/type/data?MM=1")
sleep(2)

#Navigate to data tab and allow website to reload
data_button = driver.find_element(by=By.XPATH, value = '//*[@id="wb-sm"]/div/div/ul/li[2]/a')
data_button.click()
sleep(3)

#Check child and youth box and wait for website to reload
child_button = driver.find_element(by = By.XPATH, value = '/html/body/main/div/section/div/section[1]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/ul/li[4]/a')
child_button.click()
sleep(3)

#Click on tables
table_button = driver.find_element(by=By.XPATH, value = '//*[@id="wb-auto-4"]/ul/li[2]')
table_button.click()
#sleep(3)

#Choose first table
info = driver.find_element(by = By.XPATH, value = '/html/body/main/div/section/div/section[1]/div/div[2]/div[2]/div/div[5]/div/div/div/details[2]/div/ul[1]/li[1]/div/div[1]/span/a')
info.click()
sleep(3)

#Access table data using webdriver and pandas
table = driver.find_element(by=By.ID, value = "simpleTable").get_attribute("outerHTML")
df = pandas.read_html(io.StringIO(table))

#Save data into a csv
df[0].to_csv("population_data.csv", index = False)

#Click download button
download_button = driver.find_element(by = By.ID, value = "downloadOverlayLink")
download_button.click()
download_csv = driver.find_element(by = By.ID, value = "downloadAsDisplay")
download_csv.click()