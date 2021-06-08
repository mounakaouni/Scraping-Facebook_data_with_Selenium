#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importer les libraires
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import datetime
import json
import urllib.request
from facebook_scraper import get_posts
import time
import os
import datetime 


# In[2]:


# se connecter a facebook
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})

driver =  webdriver.Chrome(chrome_options=option,executable_path = "--------/.wdm/drivers/chromedriver/80.0.3987.106/win32/chromedriver.exe")
driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
print("Opened facebook...")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys('enter your mail')
print("email entered...")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys('enter your password')
print("Password entered...")
button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("facebook opened")


# In[5]:


Results = []
post_links = []
try:
    PAGE_LOAD_WAIT = 5
    Date2 =  []
    print('go to the pages')
    List = ['list of keywords']  
    for i in List: 
         #  go to the "publications" page
        driver.get('https://www.facebook.com/search/posts/?q=%s&epa=SEARCH_BOX'% (i))
        # print('waiting...')
        time.sleep(PAGE_LOAD_WAIT)
        links = driver.find_elements_by_tag_name("a")
        for item in links:
            if item.get_attribute('data-ft') == '{"tn":",O"}':
                Voir_link = item.get_attribute('href')
                print('Keyword : ', i)
                print('post_link : ',Voir_link)
                post_links.append(Voir_link)    
        for link in post_links:
        # Name pages
            Name_page = driver.find_elements_by_tag_name("a")
            pages = link.split('/',5)
            page_name = pages[3]
            print('page_names:',page_name)
            driver.get(link)
            time.sleep(PAGE_LOAD_WAIT)
        # content 
            post_content = driver.find_elements_by_tag_name("span")
        for content in post_content:
            if content.get_attribute('class') == 'hasCaption':
                content_text = content.text
                print("content :",content_text)
        Results.append([pages[3],content_text,i,Voir_link])
# Date
    #     Date = driver.find_elements_by_tag_name("abbr")
    #     for date_ in Date:
    #         if date_.get_attribute('data-shorten') == '1':
    #             date = date_.get_attribute('title')
    #             print(date)
    #             Date2.append(date)
except StaleElementReferenceException as Exception:
    print('StaleElementReferenceException')


# In[ ]:


frame = pd.DataFrame(Results)
frame.columns = ["Page_Name","Page_content", "Keywords","link"]
# if frame['Page_content'] == None:
frame = frame.dropna(subset=["Page_content", "Keywords","link"])
frame

