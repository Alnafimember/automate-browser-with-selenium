import time

from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.google.com/gmail/about/")
driver.maximize_window()


time.sleep(5)
#Click on signin Button for gmail login
driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()

time.sleep(5)

#The username or Email for gmail login
myemail=driver.find_element(By.ID,"identifierId")
myemail.send_keys("mr5467519@gmail.com")

time.sleep(5)
#Click button to go next for entering password
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

time.sleep(5)
#Password typing
driver.find_element(By.NAME,'Passwd').send_keys('salam.123')

time.sleep(5)
#Next to login
# driver.find_element(By.CLASS_NAME,'VfPpkd-vQzf8d').click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
# driver.find_element(By.LINK_TEXT,'Next').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Next").click()
# driver.find_element(By.ID,'Next').click()
# driver.find_element(By.ID,"Next")
# driver.find_element(By.CSS_SELECTOR,'#passwordNext > div > button > span')
# driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span')
print("Login success")
time.sleep(5)
