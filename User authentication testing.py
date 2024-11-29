# Instagram Login Automation
# Author: Frank Mwito

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    
    # Step 2: Wait for the username field to be present and input the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("deinharddavid@gmail.com")
    
    # Step 3: Wait for the password field to be present and input the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("Vision@2030")
    
    # Step 4: Locate and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")) 
    )
    login_button.click()
    
    # Step 5: Optionally, wait for the homepage or another element to ensure login succeeded
    time.sleep(10)  # This is for demonstration; consider using explicit waits in real cases.
    
finally:
    # Step 6: Close the browser
    driver.quit()