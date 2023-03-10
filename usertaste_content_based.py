# -*- coding: utf-8 -*-
"""UserTaste-Content-based.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p5dRh4Tnz51WUNHSep4EMhZ-I70iqcPn

# Content Based Recommender
"""

import pandas as pd
import numpy as np

movies = pd.read_csv('movies_exploded.csv')

movies.head()

movies.info()

movies[movies['title']=='Dangerous Minds']

def show_user_taste(ur,user):
    ur = ur.set_index('title')
    user = user.set_index('title')
    urm = np.array(ur)
    userm = np.array(user)
    user_profile = urm*userm
    user_profile = user_profile.sum(axis=0)
    user_profile = user_profile/user_profile.sum(axis=0)
    user_profile = pd.DataFrame(user_profile)
    user_profile = user_profile.transpose()
    user_profile = user_profile.rename(columns={0:'Action',1:'Adventure',2:'Animation',3:'Comedy',4:'Crime',5:'Documentary',6:'Drama',7:'Faimly',8:'Fantasy',9:'Foreign',10:'History',11:'Horror',12:'Music',13:'Mystery',14:'Romance',15:'Sci:Fic',16:'TV Movie',17:'Thriller',18:'War',19:'Western'})
    return user_profile

"""## Implementing"""

rating = pd.read_csv('ratings.csv')

rating.head()

#call only user id 1 and its ratings

rating = rating[rating['userid'] ==21]

movies.head(3)

rating.head(3)

rating = rating.drop(['userid','id'],axis=1)

rating.info()

rating

ur = rating
ur.head()

rating

ur

user = rating

user

user = user.drop(['rating'],axis=1)

user

user

user = user.merge(movies)

user.index = range(len(user.index))

user

ur.info()

ur

user

def create_user_profile(ur,user):
    ur = ur.set_index('title')
    user = user.set_index('title')
    urm = np.array(ur)
    userm = np.array(user)
    user_profile = urm*userm
    user_profile = user_profile.sum(axis=0)
    user_profile = user_profile/user_profile.sum(axis=0)
    #user_profile = pd.DataFrame(user_profile)
    #user_profile = user_profile.transpose()
    #user_profile = user_profile.rename(columns={0:'Action',1:'Adventure',2:'Animation',3:'Comedy',4:'Crime',5:'Documentary',6:'Drama',7:'Faimly',8:'Fantasy',9:'Foreign',10:'History',11:'Horror',12:'Music',13:'Mystery',14:'Romance',15:'Sci:Fic',16:'TV Movie',17:'Thriller',18:'War',19:'Western',20:'[]'})
    return user_profile

def create_user_taste(ur,user,items):
    x = create_user_profile(ur,user)
    items = items.set_index('title')
    itemm = np.array(items)
    rec = x*itemm
    rec = rec.sum(axis=1)
    e = pd.DataFrame(rec,columns=['ratings'])
    items = items.reset_index()
    items['Predicted Ratings'] = e['ratings']
    items = items.set_index('title')
    return items

movies.info()

user_taste = show_user_taste(ur,user)

user_taste

user_taste.max()

s = create_user_taste(ur,user,movies)

new = s[s['Predicted Ratings'] >0.6]

new

new.sort_values(by=['Predicted Ratings'],ascending=False)