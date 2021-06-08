#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importer les libraires
import pandas as pd
import datetime
import json
import urllib.request
from facebook_scraper import get_posts
import time

# Importer les pages et les mots clés

Pages= {'write your pages'}
Mots_clés= ['write your own keywords']

# Script pour scrapper les pages et stocker les résultats dans une liste
results = []
today = datetime.datetime.now()
date_today = str(today.year) +'-'+ '0' +str(today.month) +'-'+ str(today.day)
for page in Pages:
    for post in get_posts(page,pages =1):
        print('------------------------',page,'-----------------------')
#         print('contenu:')
        for i in Mots_clés:
            if i in post['text']:
                tet = post['text']
#                 print('post_id:',post['post_id'])
                heure = str(post['time']).split( )
#                 print('Heure',heure[1])
#                 print('Date',heure[0])
#                 print('post_url:',post['post_url'])
#                 print('likes:',post['likes'])
#                 print('comments:',post['comments'])
#                 print('shares:',post['shares'])
#                 print('Image:',post['image'])
#                 print('Video:',post['link'])
#                 if str(heure[0]) == date_today:
                results.append([page,post['post_id'],tet,i, heure[0],heure[1],post['post_url'],post['likes'],post['comments'],post['shares'],post['image'],post['link']])
try: 
    # list to dataframe
    frame = pd.DataFrame(results)
    frame.columns = ["Page_Name","Post_id", "Content","Keywords","Date","Time", "Post_link","likes","comments","shares","Image_Link",'Video_Link']
    # Supprimer les redandances du dataframe
    frame2 = frame.drop_duplicates(subset ="Post_id")
    filename2 = str(today.day) +'-'+ '0' +str(today.month) +'-'+ str(today.year)
    if os.path.isfile(filename2):
        print ("File exist")
    else:
        print ("File not exist") 
    # Dataframe to excel, stocker le fichier par  date
    facebook_output = frame2.to_excel(str(filename2) +'.xlsx', header=True, index=False)
except ValueError:
    print('there is no information today')

while True:
    print("i will scrap the data after 2 hours")
#     time.sleep(60) # Delay for 2 hours
    time.sleep(3600*2) # Delay for 2 hours


# In[ ]:




