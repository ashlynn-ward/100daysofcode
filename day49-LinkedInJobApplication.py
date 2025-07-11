#LinkedIn Job Application
#Ashlynn Ward, June 28, 2025
#This program uses Selenium webdriver to automatically apply for jobs on LinkedIn. Note - you must enter your credentials for it to work.
#Before using this program, add your resume to your account so it is automatically added to applications. Also, turn off 2-step verification.

#Import modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

#Function abort application deletes the application form and exits it
def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create driver
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4255495964&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
sleep(2)

#Try to enter credentials for sign-in
try:
    sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
    sign_in.click()
    sleep(2)
    username = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
    username.send_keys("enter phone or email here")
    password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
    password.send_keys("enter password here")
    sign_in_2 = driver.find_element(By.CSS_SELECTOR, value="#sign-in-form button")
    sign_in_2.click()
    sleep(2)
except NoSuchElementException:
    print("Already signed in.")

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys("enter phone number here")

        #Save application
        save_button = driver.find_element(By.CSS_SELECTOR, value=".mt4 .display-flex .jobs-save-button")
        save_button.click()

        sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

