#Map Directions
#Ashlynn Ward, July 1, 2025
#This program prompts the user for their start and end destination. It then enters that into MapQuest, and prints out the ETA and whether
#traffic is heavy.

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
driver.get("https://www.mapquest.com/")
sleep(2)

#Ads may pop up, instruct user to manually exit them
input("An ad may pop up when the website loads. Press enter after you exit the ad.")

#Click MapQuest button
quest_button = driver.find_element(by = By.CSS_SELECTOR, value = "#rail-content button")
quest_button.click()
sleep(2)

#Prompt user for starting and ending destinations
beginning = input("Enter your starting address: ")
end = input("Enter destination address: ")

#Enter destinations in MapQuest
beginning_input = driver.find_element(by = By.ID, value = "location-A")
beginning_input.send_keys(beginning)
beginning_choose = driver.find_element(by = By.CSS_SELECTOR, value = '/html/body/div[2]/div/div/div[2]/ul/li')
beginning_choose.click()
end_input = driver.find_element(by = By.ID, value = "location-B")
end_input.send_keys(end)
end_choose = driver.find_element(by = By.CSS_SELECTOR, value = '/html/body/div[2]/div/div/div[2]/ul/li')
end_choose.click()
sleep(2)

#If invalid address is entered, ETA will not show up. If this occurs, ask for addresses until valid ones are given
exists = False
while exists == False:
    sleep(2)
    try:
        #If ETA shows up, print it out
        eta = driver.find_element(by = By.XPATH, value = "/html/body/aside/div[1]/div[3]/div[3]/div[4]/div[3]/strong")
        print(f"ETA from {beginning} to {end} is {eta.text}")
        exists = True
    except NoSuchElementException:
        print("Invalid addresses inputted.")
        beginning = input("Enter your starting address: ")
        end = input("Enter destination address: ")
        #Send new addresses
        beginning_input.clear()
        beginning_input.send_keys(beginning)
        beginning_choose = driver.find_element(by = By.CSS_SELECTOR, value = '/html/body/div[2]/div/div/div[2]/ul/li')
        beginning_choose.click()
        end_input.clear()
        end_input.send_keys(end)
        end_choose = driver.find_element(by = By.CSS_SELECTOR, value = '/html/body/div[2]/div/div/div[2]/ul/li')
        end_choose.click()

#If MapQuest says anything other than light traffic, print a message saying that there will be traffic
traffic = driver.find_element(by = By.XPATH, value = '/html/body/aside/div[1]/div[3]/div[3]/div[4]/div[3]/div')
if traffic.text !="Light traffic":
    print(f"TRAFFIC WARNING: MapQuest detects {traffic.text}")