from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH="C:/Program Files/chromedriver/chromedriver.exe"
driver=webdriver.Chrome(PATH)  
driver.get('http://www.google.com/')
search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
search.send_keys("spacex")
search.send_keys(Keys.RETURN)
try:
    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )
    print(contents.text)
except:
    pass
