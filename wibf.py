from selenium import webdriver
import pyautogui
import time 
import pyperclip
from selenium.webdriver.chrome.options import Options   
driver=webdriver.Chrome()

def wib(Xpath,text):
    driver.find_element_by_xpath(Xpath).send_keys(text)
    
def write(text):
 pyautogui.typewrite(text)
def ok():
 pyautogui.press("enter")
def gt():
 time.sleep(0.3)

def ow(link):
    driver.get(link)
def tkla (Xpath):
    ltc= driver.find_element_by_xpath(Xpath)
    ltc.click()

def ont():
    pyautogui.hotkey('ctrl', 't')



    


    


