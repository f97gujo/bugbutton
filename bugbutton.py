#! python
import sys
import os
import errno
from datetime import datetime
from os import mkdir
import shutil
import win32api

#This program is for when finding a bug, it will move logs to separate folder, start screenshot program, and accept user input what the bug was about

#Variables
bug_folder = r'C:\Users\gunnar.johansson\Desktop\bugs'


#If folder for bugs does not exist, create it

if not os.path.exists(bug_folder):
    os.makedirs(bug_folder)

#Create a timestamped folder for the current issue
now = datetime.now
issue_folder = r'C:/Users/gunnar.johansson/Desktop/bugs/{}'.format(now().strftime("%Y-%m-%d-%H.%M.%S"))
mkdir(issue_folder)

#Copy Analyze client log
shutil.copy2(r'C:\ProgramData\Griffeye Technologies\Griffeye Analyze\Error\LogFile.txt', issue_folder)
#Copy Analyze server log
#shutil.copy2('C:\ProgramData\Griffeye Technologies\Griffeye Analyze Collaboration Server\EventLogs\applog.txt', issue_folder)
#Copy NMS log
shutil.copy2(r"C:\ProgramData\NetClean Technologies\NetClean ProActive Management Server\EventLogs\nms_log.txt", issue_folder)
#Copy NMC log
shutil.copy2(r"C:\ProgramData\NetClean Technologies\NetClean ProActive Management Console\Error\nmc_log.txt", issue_folder)

#Start screenshot
#os.startfile('C:\Program Files\Greenshot\Greenshot.exe')
printscreen = 0x2C # VirtualKey Code of the printscreen button, see     http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx 
win32api.keybd_event(printscreen,0,0,0) # holds the "printscreen" key down

#Get user input what the bug was about
#Create textfile for input
filepath = os.path.join(issue_folder, 'Issue.txt')
f = open(filepath,'w')
#Prompt user
input_var = input("What is the issue: ")
f.write(str(input_var))
f.close()
