from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH="C:/Program Files/chromedriver/chromedriver.exe"
driver=webdriver.Chrome(PATH)  
driver.get('http://www.google.com/')
search=driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys("weather in south bopal")
search.send_keys(Keys.RETURN)
driver.set_window_position(-2000,0)
try:
    loc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_loc"))
    )
    dcp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_dcp"))
    )
    tm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_tm"))
    )
    pp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_pp"))
    )
    hm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_hm"))
    )
    ws = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_ws"))
    )
    dp = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "wob_dp"))
    )
    print(loc.text)
    print(dcp.text)
    print("the current temperature is",tm.text,"degree celsius")
    print("the chances of rain is",pp.text)
    print("the humidity level is",hm.text)
    print("the current wind speed is",ws.text)
    print("the weather forecast for upcoming days are",dp.text)
except:
    pass
