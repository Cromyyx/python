import logging
from datetime import datetime
logging.basicConfig(filename='script.log', level=logging.INFO)
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logging.info(f'{current_time} - Script started')

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your WebDriver executable
webdriver_path = r'C:\Program Files\edgedriver_win64\msedgedriver.exe'

# URL of the login page
login_url = "https://merano.multiutilitycard.it/menuAziende/login/login#!/pages"

# Your login credentials
username = "34466"
password = "gx6sro0r"

# Initialize the WebDriver
service = Service(webdriver_path)
driver = webdriver.Edge(service=service)

# Open the login page
driver.get(login_url)

# Find the username and password input fields and enter your credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the page to load and the "Prenota un pasto" button to be clickable
wait = WebDriverWait(driver, 10)
prenota_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.box.bg-success")))

# Click the "Prenota un pasto" button
prenota_button.click()

# Wait for the radio buttons to be present
radio_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".custom-control-input")))

# Use JavaScript to click the second radio button
driver.execute_script("arguments[0].click();", radio_buttons[1])

# Wait for the third radio button to appear
next_radio_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".custom-control-input.ng-pristine.ng-untouched.ng-valid.ng-empty")))

# Use JavaScript to click the third radio button
driver.execute_script("arguments[0].click();", next_radio_button)

#logging reaches 3rd Button
logging.info(f'{current_time} - Skript reaches 3. button')

# Wait for the confirmation button to be clickable
confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-success.btn-block.m-t-2.ng-scope")))

# Use JavaScript to click the confirmation button
driver.execute_script("arguments[0].click();", confirm_button)

# Keep the browser window open for 30 seconds for testing purposes
#time.sleep(5)

# Close the WebDriver
driver.quit()

#logging reaches finishes correctly
logging.info(f'{current_time} - Script stopped without timeout')
