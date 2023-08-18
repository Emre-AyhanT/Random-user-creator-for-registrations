from selenium import webdriver
import time
from wibf import ow,wib,gt,tkla,ont
from KeepD import Names,Surnames,Emails,UsrPasswds,nlin,EmailsWoFo,Numbers
import pyautogui
import random
from selenium.webdriver.chrome.options import Options       
def type_text(text):
    pyautogui.typewrite(text)
def ok():
 pyautogui.press("enter")
def click_button(x, y):
    pyautogui.click(x, y)
def ct():
    pyautogui.hotkey('ctrl', '1')
def ct2():
    pyautogui.hotkey('ctrl', '2')
def copy():
    pyautogui.hotkey('ctrl', 'c')
def closet():
    pyautogui.hotkey('ctrl', 'w')
def paste():
    pyautogui.hotkey('ctrl', 'v')
def icn():
    pyautogui.hotkey('ctrl', 'shift', 'n')

    



ow("https://www.google.com.tr/")
time.sleep(1)
"""
click_button(924,39)
time.sleep(1)
click_button(408,1040)
time.sleep(1)
icn()
type_text('go')
ok()
time.sleep(1)
click_button(1831,133)
time.sleep(1)
click_button(833,720)

time.sleep(1)
click_button(863,765)
time.sleep(1)
click_button(863,537)
time.sleep(1)
type_text(Names[0])
click_button(1105,692)
time.sleep(1)

click_button(831,521)
type_text('1')
click_button(968,521)
click_button(957,591)
click_button(1067,517)
type_text('2000')

click_button(939,596)
click_button(902,648)
click_button(1099,671)
time.sleep(1)


click_button(866,742)
time.sleep(0.5)
ont()
type_text('tmmail')
ok()
time.sleep(1)
click_button(470,379)
time.sleep(1.5)
click_button(330,142)
time.sleep(1.5)

ct()
time.sleep(1)
click_button(330,736)
time.sleep(0.5)
paste()
time.sleep(0.5)
click_button(330,142)

type_text(EmailsWoFo[0])
type_text('.1957q')
time.sleep
click_button(1113,770)
time.sleep(1)

type_text(UsrPasswds[i])
click_button(905,612)
type_text(UsrPasswds[i])
click_button(1116,738)










"""
























#time.sleep(2)
#tkla('//*[@id="gb"]/div/div[2]/a/span')
#tkla('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span')

















































































"""
wib("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input",Names[0])
gt()
wib("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input",Surnames[0])
tkla("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[3]/div/div/button/span")
gt()
wib("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input",Emails[0])
wib("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input",UsrPasswds[0])
wib("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",UsrPasswds[0])
gt()
ont()
type_text(nlin)
ok()
time.sleep(2)
click_button(878, 164)
time.sleep(1)
click_button(709, 291)
time.sleep(1)
click_button(383, 581)
time.sleep(1)
type_text(EmailsWoFo[0])
gt()
click_button(464,657)
type_text(UsrPasswds[0])
ok()
ct()
time.sleep(0.5)
tkla("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
time.sleep(1)
ct2()
time.sleep(3)
click_button(115,266)
time.sleep(2)
click_button(640,320)
time.sleep(3)
click_button(640,320)
time.sleep(3)
click_button(103,67)
time.sleep(3)
for k in range(1, 7):
   click_button(858,642)
for t in range(1,3):
 click_button(596,627)
copy()
time.sleep(0.2)
closet()
time.sleep(0.5)
paste()
ok()










"""