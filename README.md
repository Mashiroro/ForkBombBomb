# BirdPooper
This was a project that my friend (SudoIndividual) and I did back in june/july 2020. Why is it called birdpooper? Because when bird poops on you, you will struggle to clean the poop off your clothes. Thus, this malware will make you struggle to clean the "poop"/malware off your computer. 

### Purpose
We created BirdPooper just for fun and to gain experience in both python and batch. We do not intent to cause harm to others!

### How it works
Windows:
![image](https://user-images.githubusercontent.com/45526280/139047257-095a1a53-8e8b-4d93-b756-3a5e076738f7.png)
###### Outcome:
- Simultaneously generate hundreds / thousands of .bat files in multiple directories
- Launch multiple Command Prompts
- Severe lag to the infected computer
- In Virutal Machines (VM) you may get a black screen.


### Removal
Windows:
1. Reboot computer / VM to safe mode
2. Go to AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
3. Delete Everything
4. Good luck with the lag <3

### FYI
This will not work properly. Why?
1. I am too lazy to compile all 33 scripts into .exe
2. It gets annoying to test and clean this BirdPooper
3. i got lazy to continue this project lol

To work it (maybe):
1. Disable anti-virus 
on Administrator Powershell do:
```
Set-MpPreference -disablerealtimemonitoring $true
```
3. Compile all 33 scripts into individual .exe files
4. Make sure all 33 scripts are in the same directory
5. have fun :P

### DISCLAIMER
BirdPooper is a virus/malware that can harm both Windows and
Linux OS! We created this for fun and to better understand Python.
We highly recommend you to use this on a Virtual machine only! We
will not be responsible for any harm or damages done on to you or 
anyone's computers. Use this at your risk! You have been warned!
