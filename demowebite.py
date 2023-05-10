import time

from selenium import webdriver
# from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(5)
#This is for user-name
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(5)
#This is for password

driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)

#login

driver.find_element(By.ID,"login-button").click()



# time.sleep(40)



