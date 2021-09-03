from selenium import webdriver
import config
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome


chrome_driver_binary = config.CHROMEDRIVER_BINARY_LOCATION

# browser = Chrome(chrome_driver_binary)
# browser.get('https://www.browserstack.com')
# print(browser.title)
# button = browser.find_element_by_id('signupModalButton')
# button.click()
# browser.close()



options = webdriver.ChromeOptions()
u = "https://www.google.com/maps/place/Migros+Supermarkt/@47.3965551,8.5372507,15z/data=!3m1!5s0x47900a19c8f4618d:0x7c71af455e4f3cd2!4m9!1m2!2m1!1smigros!3m5!1s0x0:0x5c5c19940cc5f58b!8m2!3d47.391336!4d8.518553!15sCgZtaWdyb3MiA4gBAVoIIgZtaWdyb3OSAQ1ncm9jZXJ5X3N0b3Jl"
d = webdriver.Chrome(chrome_driver_binary, options=options)
se = d.get(u)
time.sleep(2)

elem = d.find_elements_by_class_name("VfPpkd-LgbsSe-OWXEXe-k8QpJ")[3]
elem.click()
time.sleep(5)