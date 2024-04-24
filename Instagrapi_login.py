from instagrapi.exceptions import LoginRequired
import logging
from instagrapi import Client
from instagrapi.extractors import extract_user_short
import json
import time
import os
def login_user(USERNAME, PASSWORD, cl, logger):
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """
    session_path="" #put the path of the session.json file here
    login_via_session = False
    login_via_pw = False

    if os.path.exists(session_path) and os.path.getsize(session_path) > 0:
        session = cl.load_settings(session_path) 
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)
            try:
                # Check if session is valid
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")
                cl.set_settings({})
                cl.set_uuids(session["uuids"])  #use the same device across logins
                cl.login(USERNAME, PASSWORD)
                login_via_pw = True
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)
            login_via_session = False

    if not login_via_session and not login_via_pw:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            cl.login(USERNAME, PASSWORD)
            login_via_pw = True
            
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)
            
    if login_via_pw and os.path.exists(session_path):
        # Save session settings
        session = cl.get_settings()
        with open(session_path, "w") as json_file:
            json.dump(session, json_file)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

def main(): #this main was created just for debugging

    logger = logging.getLogger()
    cl = Client()
    
    USERNAME = ""
    PASSWORD = ""
    
    
    login_user(USERNAME, PASSWORD,cl,logger)
    user_id = cl.user_id_from_username(USERNAME)
    print(user_id) 

if __name__ == "main":
    main()