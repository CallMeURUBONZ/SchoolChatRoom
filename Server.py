Username = input("Enter Username: ")
from datetime import datetime
import os
currentcwd = os.getcwd()
now = datetime.now()
import sys
from flask import Flask, render_template
testvar = "hello"
current_time = now.strftime("%H:%M:%S")





while True:
    logfile = open("Log.txt", "a+")
    for x in range(1):
        Message = input("Message: ")
        logfile.writelines(f'{current_time}|||{Username}: {Message}\n')
        logfile.close()



