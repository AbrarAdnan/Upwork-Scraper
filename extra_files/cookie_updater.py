from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import os

mail = os.getenv("MAIL")
password = os.getenv("PASSWORD")

def update_cookie():
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    print("logging in with credentials")
    # Access variables
    driver.get('https://www.upwork.com/ab/account-security/login')
    username = driver.find_element(By.ID,"login_username")
    username.send_keys(mail)
    time.sleep(1.5)
    login_button = driver.find_element(By.ID,'login_password_continue')
    login_button.click()
    time.sleep(1.5)
    login_password = driver.find_element(By.ID,"login_password")
    login_password.send_keys(password)
    time.sleep(1.5)
    remember_btn = driver.find_element(By.CLASS_NAME,'up-checkbox-replacement-helper')
    remember_btn.click()
    final_login_button = driver.find_element(By.ID,'login_control_continue')
    final_login_button.click()
    print('logged in with credentials')
    time.sleep(3)
    # Get the cookies from the browser
    cookies = driver.get_cookies()
    # Write the cookies to a json file
    with open("cookies.txt", "w") as f:
        json.dump(cookies, f)
    print("Updated cookies")
    driver.close()


if __name__ == "__main__":
    update_cookie()