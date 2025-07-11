#Import webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create driver
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.python.org/")

#Access upcoming events
upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
#Access dates for events
dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = {}

#Add events and dates to a dictionary
for n in range(0,len(upcoming_events)):
    events[n] = {"time":dates[n].text,
        "event":upcoming_events[n].text
    }
#Close browser
driver.quit()