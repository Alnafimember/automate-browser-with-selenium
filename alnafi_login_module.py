import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://alnafi.com/sign-in")
driver.maximize_window()

#The username or Email is
myemail=driver.find_element(By.ID,"Username/ Email")
myemail.send_keys("Muhammad__")
time.sleep(5)

#Password of alnafi is

mypassword=driver.find_element(By.ID,"Password")
mypassword.send_keys("Peanut@345")
time.sleep(5)

#Click on login button

login=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/form/div[3]/button")
login.click()
time.sleep(25)
