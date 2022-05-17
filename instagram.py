import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver_path = 'C:/Users/es_lo/Desktop/geckodriver.exe'

browser = webdriver.Firefox(executable_path=driver_path)
browser.get("https://www.instagram.com/")
browser.implicitly_wait(3)
# Login Page
username = browser.find_element(By.NAME,"username").send_keys("Account_name")
password = browser.find_element(By.NAME,"password").send_keys("Account_password")
submitButton = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
browser.implicitly_wait(5)


# Mainpage 
try:
    notification = browser.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/button[2]").click()
finally:
    profile_icon = browser.find_element(By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img").click()
    browser.find_element(By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div").click()
    browser.implicitly_wait(5)
# Go To Profile
following = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").click()


# Javascript Commands
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage = followers.scrollHeight;return lenOfPage;
"""
lenOfPage = browser.execute_script(jscommand)
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

# getFollowingList
followingList = browser.find_elements_by_class_name("_0imsa")
with open("following.txt","w",encoding="utf-8") as file:
    for i in followingList:
        file.write(i.text + "\n")
        time.sleep(1)

 

time.sleep(5)
browser.close()