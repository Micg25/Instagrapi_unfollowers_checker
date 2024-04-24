from instagrapi import Client
from instagrapi.extractors import extract_user_short
import json
import time
import os
import Instagrapi_login as pl
import numpy as np
ACCOUNT_USERNAME="" #replace with your own Username
ACCOUNT_PASSWORD="" #replace with your own Password
cl = Client()
logger = pl.logging.getLogger()
pl.login_user(ACCOUNT_USERNAME, ACCOUNT_PASSWORD,cl,logger)
time.sleep(10)

user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
print(user_id)

state_file = "state.txt"


if os.path.exists(state_file):
    users_id1=[]
    users_id2=[]
    fw=cl.user_followers(user_id, amount = 0)
    for user in fw:
        users_id2.append(user)

    with open("follower1.txt","r") as file:
        for line in file:
           users_id1.append(line.strip())

    set1=set(users_id1)
    set2=set(users_id2)
    unfollowers= set1 - set2
    i=1
    if len(unfollowers>0):
        for x in unfollowers:
            print(f"UNFOLLOWER No {i} : {cl.username_from_user_id(x)}")
            i+=1 
        with open("follower1.txt", "w") as file:
            for x in set2:
                file.write(str(x) + "\n")
else:
    fw=cl.user_followers(user_id, amount = 0)
    users_id1=[]
    for user in fw:
        users_id1.append(user) 
    set1=set(users_id1)
    with open("follower1.txt", "w") as file:
        for x in set1:
            file.write(str(x) + "\n")
    with open(state_file,"w") as file:
        file.write("The code has been run before")