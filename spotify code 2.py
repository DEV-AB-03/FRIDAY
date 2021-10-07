from pywinauto.application import Application  
import pyautogui
import time
app = Application().start('Spotify.exe')
pyautogui.moveTo(30,301,duration=15)
pyautogui.doubleClick(button="left")

