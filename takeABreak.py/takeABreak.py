#Simple script to open a browser window with a youtube video
#every 2 hours so you can take a break. Change the video url as
#well as the amount of breaks

import webbrowser
import time

total_breaks = 3
x = 0
print("The program has started, it started at: "+ time.ctime())
while(x < total_breaks):
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=xlQ_NlX4MFw&index=74&list=LLGd54qpH1rBS9hFRZFU2dQQ")
	print("It's now break time and the current time is: "+time.ctime())
	x += 1