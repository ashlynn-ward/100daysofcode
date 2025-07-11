#Job Board Listings
#Ashlynn Ward, June 29, 2025
#This program accesses the job lisitings on Indeed based on a key word given. 

#Import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create driver
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://ca.indeed.com/?r=us")
sleep(2)

#Prompt user to enter their location and job type
location = input("Enter the location wher you are looking for a job? Enter location in City, Province Code format: ")
keyword = input("Enter a keyword to narrow job listings: ")

#Access input boxes
search_box = driver.find_element(By.ID, value = "text-input-what")
search_box.send_keys(keyword)
location_box = driver.find_element(By.ID, value="text-input-where")
location_box.send_keys(location)
#Instead of having the webdriver click "search", you must manually do it to bypass Catchya
input("Click enter once you have clicked search")
sleep(2)

#Find all job listings
job_listings = driver.find_elements(By.CLASS_NAME, value = "jobTitle")
salaries = driver.find_elements(By.CLASS_NAME, value="salary_snippet-container")

#Add jobs and salaries to a dictionary
jobs = {}

for n in range(len(job_listings)):
    jobs[n]={
        "Title":job_listings[n],
        "Salary":salaries[n]
    }

#Print jobs
print(f"Here are the current listings for {keyword} in {location}:\n{jobs}")