In order to properly run the Unfollowers Checker, put session.json,follower1.txt, instagrapi_login.py and Unfollowers_checker.py in the same folder. 

In the Unfollowers_checker code replace USERNAME="" and PASSWORD="" with your own instagram's username and passowrd; in the instagrapi_login code instead put the path of the session.json file where needed (I made a comment beside the variable where you must put it).
Once you've done all these things just start Unfollowers_checker.py, if you are running it for the first time the program will store your current followers in "followers.txt", and then it will create a file "state_file.txt" wich will tell if the code was run before so it won't have to store the followers again. 
For the next executions of the program this will just re-calculate the current followers and it will compare to the pre-existant "follower1.txt", if it will find some differences it will print you the usernames of the unfollowers and then it will replace "follower1.txt" with the updated one.

If you are wondering if this procedure could have been done in "running-time"/"real-time", I mean that you start the program and this enters in a cycle where it check every second your followers to check if there are unfollowers, this sadly can't be apparently done with Instagrapi. But if you do know a method to do that with instagrapi and you want to share it, do it
