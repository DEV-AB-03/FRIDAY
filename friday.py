import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pywinauto.application import Application  
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    date = datetime.date.today()
    x = datetime.datetime.now()
    day=x.strftime("%A")
    strtime=datetime.datetime.now().strftime("%H:%M:%S")
    t = time.strptime(strtime, "%H:%M:%S")
    timevalue_12hour = time.strftime( "%I:%M %p", t )

    if  hour>=0 and hour<12:
        speak('Good Morning boss')
        speak('i am friday ')
        speak("Today's date is")
        print(date)
        speak(date)
        print(timevalue_12hour)
        speak(timevalue_12hour)
    elif hour>=12 and hour<18:
        speak("good afternoon boss ")
        speak('i am friday')
        speak("Today's date is")
        speak(date)
        print(date)
        speak("the current time is")
        speak(timevalue_12hour)
        print(timevalue_12hour)
    elif hour>=18 and hour<22:
        speak("good evening boss")  
        speak('i am friday')  
        speak("today is")
        speak(day)
        speak("Today's date is")
        speak(date)
        print(date)
        print(timevalue_12hour)
        speak("the current time is")
        speak(timevalue_12hour)
    elif hour>=22 and hour<=24:
        speak("good evening boss")  
        speak('i am friday')  
        speak("Today's date is")
        speak(date)
        print(date)
        speak("the current time is")
        speak(timevalue_12hour)
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....') 
        r.adjust_for_ambient_noise(source)
        r.energy_threshold=200
        r.dynamic_energy_threshold=500
        r.pause_threshold = 1
        audio=r.listen(source) 
    try:
        print('Recognizing')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print('Say that again please')
        return "none"
    return query

if __name__ == "__main__":
    wishme()
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
                lo="the current location is"+loc.text
                dc="the current weather condition is"+dcp.text
                ctm="the current temperature is"+tm.text+"degree celsius"
                cr="the chances of rain is"+pp.text
                chm="the humidity level is"+hm.text
                cws="the current wind speed is"+ws.text
                print(lo)
                print(dc)
                print(ctm)
                print(cr)
                print(chm)
                print(cws)
                speak(lo)
                speak(dc)
                speak(ctm)
                speak(cr)
                speak(chm)
                speak(cws)
                speak("do you want to know the forecast for the upcoming week")
                c=takeCommand()
                if "yes" in c:
                    wf="the weather forecast for upcoming days are"+dp.text
                    speak(wf)
                    driver.quit()
                elif "no" in c:
                    speak("ok boss")
                    driver.quit()
    except:
        pass   
    
    speak('what would you like me to do for you')

    while True:
        query=takeCommand().lower()
        if 'who is' in query:
            speak("searching")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("Here is what i found....")
            speak(results)
            print(results)

        elif 'bye'in query:
            speak("ok boss")
            speak("happy to help")
            speak("i am here if you need me")
            break
        elif 'mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("here u go boss")
            speak("need something else boss")
        elif 'weather' in query:
            print(query)
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
                print(loc.text)
                speak("the current location is")
                speak(loc.text)
                dcp = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_dcp"))
                )   
                print(dcp.text)
                speak("the weather condition is")
                speak(dcp.text)
                tm = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_tm"))
                )   
                print("the current temperature is",tm.text,"degree celsius")
                speak("the current temperature is")
                speak(tm.text)
                speak("degree celsius")

                pp = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_pp"))
                )
                print("the chances of rain is",pp.text)
                speak("the chances of rain is")
                speak(pp.text)
                hm = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_hm"))
                )
                print("the humidity level is",hm.text)
                speak("the humidity level is")
                speak(hm.text)
                ws = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_ws"))
                )
                print("the current wind speed is",ws.text)
                speak("the current wind speed is")
                speak(ws.text)
                dp = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "wob_dp"))
                )
                print("the weather forecast for upcoming days are",dp.text)
                speak("the weather forecast for upcoming days are")
                speak(dp.text)
            except:
                pass

        elif 'vttop' in query:
            webbrowser.open("http://vtopcc.vit.ac.in:8080/vtop/initialProcess")
            speak("here u go boss")
            speak("need something else boss")
        elif 'videos of' in query:
            query=query.replace("videos of","")
            PATH="C:/Program Files/chromedriver/chromedriver.exe"
            driver=webdriver.Chrome(PATH)    
            driver.get('http://www.youtube.com/')
            search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            search.send_keys(query)
            search.send_keys(Keys.RETURN)
            speak("here u go boss")
            speak("need something else boss")
        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/?hl=en")
            speak("here u go boss")
            speak("need something else boss")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is{strtime} boss")
        elif 'mail' and 'vit' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            speak("here u go boss")
            speak("need something else boss")
        elif "music" in query:
            app = Application().start('Spotify.exe')
            pyautogui.moveTo(30,301,duration=25)
            pyautogui.doubleClick(button="left")



                



