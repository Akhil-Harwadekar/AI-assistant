import pyttsx3
import datetime
import os
import random
import time
import webbrowser
import wikipedia

engine = pyttsx3.init() # object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 180)     # setting up new voice rate

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices.

print('\t \t \t Welcome to Akhil\'s Program')
print('\t \t \t----------------------------')	

def greet():
    name="Akhil"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        pyttsx3.speak("Good Morning "+name+". I am your virtual Assistant")
    elif hour>=12 and hour<18:
        pyttsx3.speak("Good Afternoon "+name+". I am your virtual Assistant") 
    else:
        pyttsx3.speak("Good Night"+name+". I am your virtual Assistant") 

def speak(audio):  
  engine.say(audio)
  engine.runAndWait()
  time.sleep(1)

def donot(ip):
  if(("dont" in ip) or ("do not" in ip) or ("don\'t" in ip)):
    speak("Okay...")
    exit()
  else:
    return 

if __name__ == "__main__":
  greet()
  print()
  print("\t ~~~ These are the most prominent tasks that I do for you ~~~")  
  print(" 1) Browser \t 2) Editors \t 3) Media Players \t 4) Date \t 5) Time \t 6) Calender \t 7) Wikipedia \t 8) Instagram \t 9) WhatsApp \t 10) Facebook")
  print("11) Youtube Search \t 12) Gmail \t 13) Calculator \t 14) MS-Paint \t 15) Font-Colour \t 16) Create Folder \t 17) Delete Folder \t 18) Open Folder \t 19) File Explorer \t 20) Create Secured Folder")   
  print("21) Camera \t 22) IP-configuration \t 23) Ping \t 24) Website \t 25) WiFi \t 26) Hotspot \t 27) Available Networks \t 28) Search Apps in Store \t 29) Weather \t 30) Songs")
  print("31) Set Alarm \t 32) Python \t 33) Control-Panel \t 34) Settings \t 35) Running Process \t 36) Clear Screen \t 37) LogOut \t 38) Restart \t 39) Shut-Down \t 40) Exit")
  print()
  while True:
    pyttsx3.speak("How can I help you ?")
    print()
    print("Enter the task you wish to perform :- ",end='')
    ip=input().lower()

    if (("run" in ip) or ("launch") or ("open")) and ( ("chrome" in ip) or ("google" in ip)):                                           #chrome
      donot(ip)
      speak("Opening Google Chrome")
      os.system("chrome")

    elif (("run" in ip) or ("launch") or ("open")) and ( ("edge" in ip) or ("microsoft edge" in ip) or ("microsoftedge" in ip)):        #edge
      donot(ip)  
      speak("Opening Microsoft Edge")
      os.system("microsoftedge")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and ("browser" in ip):                                                   #browser
      donot(ip)
      speak("Two browsers detected. Google Chrome and Microsoft Edge. Which one to open?")
      print("1. Chrome \t 2.Edge \t :- ", end='')
      editor=input().lower()
      if ("1" in editor) or ("chrome" in editor) or("google chrome" in editor):
        speak("Opening Google Chrome")
        os.system("chrome")
      elif ("2" in editor) or ("edge" in editor) or ("microsoft edge" in editor) or ("microsoftedge" in editor):
        speak("Opening Microsoft Edge")
        os.system("microsoftedge")
      else:
        speak("Sorry, I don't understand")
        exit()

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("notepad" in ip) or ("notepad-editor" in ip) or ("file" in ip)):       #notepad / any file
      donot(ip)
      speak("Opening Notepad")
      os.system("notepad")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("wordpad" in ip) or ("wordpad-editor" in ip)):                      #wordpad
      donot(ip)
      speak("Opening Wordpad")
      os.system("wordpad")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("editor" in ip) or ("text" in ip)):                                 #text editor
      donot(ip)
      speak("Two editors detected. Notepad and Wordpad. Which one to open?")
      print("1. Notepad \t 2.Wordpad \t :- ", end='')
      editor=input().lower()
      if ("1" in editor) or("notepad" in editor):
        speak("Opening Notepad")
        os.system("notepad")
      elif ("2" in editor) or("wordpad" in editor):
        speak("Opening Wordpad")
        os.system("wordpad")
      else:
        speak("Sorry, I don't understand")
        exit()
      		
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("windows player" in ip) or ("windows  media" in ip)):                       #win player
      donot(ip)
      speak("Opening Windows Media Player")
      os.system("wmplayer")
 
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and ("vlc" in ip):                                                            #vlc
      donot(ip)
      speak("Opening VLC Player")
      os.system("vlc")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("media" in ip) or ("player" in ip)):                                        #media
      donot(ip)
      speak("Two media players detected. VLC and Windows Media Player. Which one to open?")
      print("1. VLC\t 2.Windows Media Player \t :- ", end='')
      editor=input().lower()
      if ("1" in editor) or ("vlc" in editor) or("VLC" in editor):
        speak("Opening VLC Player")
        os.system("vlc")
      elif ("2" in editor) or ("windows" in editor) or("windowsmediaplayer" in editor):
        speak("Opening Windows Media Player")
        os.system("wmplayer")
      else:
        speak("Sorry, I don't understand")
        exit()

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and ("python" in ip):                                                              #python 
      donot(ip)
      speak("Opening Python Prompt")
      os.system("python")

    elif ("clear" in ip) or ("screen" in ip) or ("cls" in ip):                                                                          #clear screen 
      donot(ip)
      speak("Clearing the screen")
      os.system("cls")

    elif (("show" in ip) or ("display" in ip)) and ("date" in ip):                                                                          #date
      donot(ip)
      speak("Showing today's date")
      os.system("date /t")

    elif (("set" in ip) or ("keep" in ip)) and ("alarm" in ip):                                                                          #set alarm
      donot(ip)
      speak("Set your Alarm time")
      os.system("start ms-clock:")

    elif (("show" in ip) or ("display" in ip)) and (("time" in ip) or ("clock" in ip) or ("watch" in ip)):                                    #time
      donot(ip)
      speak("Time is ")
      os.system("time /t") 
    
    elif (("show" in ip) or ("display" in ip) or ("open" in ip)) and (("cal" in ip) or ("calender" in ip)):                                    #calender
      donot(ip)
      speak("Opening the calender")
      os.system("start outlookcal:") 

    elif (("change" in ip) or ("apply" in ip)) and (("clr" in ip) or ("color" in ip) or ("colour" in ip)):                              #color
      donot(ip)
      speak("Pick the number you would like to change your text colour to?")
      print("0-Black \t 1-Blue \t 2-Green \t 3-Aqua \t 4-Red")
      print("5-Purple \t 6-Yellow \t 7-White \t 8-Gray \t 9-Light Blue \t :- ",end='')
      fg=input()
      if int(fg) in range(10):
        os.system("color "+fg)    
        speak("Colour changed Successfully !")
      else:
        speak("Sorry, Invaild input")
        exit()

    elif ("hello" in ip):                                                                                                           #greet1
      speak('Hi there ! Nice to meet you')    

    elif ('how are you' in ip):                                                                                                     #greet2
      stMsgs = ['I am feeling good and I\'m getting better!', 'Not too shabby at all ', 'I am Good, with full of energy','I am super cool!']     
      ans_q = random.choice(stMsgs)
      speak(ans_q)
      speak('How are you ?')
      print('How are you ? ',end='')
      resp=input().lower()
      if ("happy" in resp) or ("cool" in resp) or ("super" in resp) or ("fantastic" in resp) or ("fine" in resp)  or ("good" in resp):
        speak("Wow, that\'s great !")
      elif ("sad" in resp) or ("not" in resp) or ("upset" in resp) or ("disappoint" in resp) or ("no" in resp):
        speak("ohhh..! i'm Sorry")
      else:
        speak('Okay Good')     

    elif ('built' in ip) or ('created' in ip) or ('developed' in ip):                                                                   #greet3
      ans_m = "master Akhil gave me a life! And I am very much greatful to him "
      speak(ans_m)
      print(ans_m)

    elif ('beautiful' in ip) or ('sweet' in ip) or ('good' in ip):                                                                   #greet4
      ans_m = "Oh wow. You can't tell but I\'m totally blushing right now "
      speak(ans_m)
      print(ans_m)

    elif ("who are you" in ip) or ("about you" in ip) or ("your details" in ip) or ("something" in ip):                         #greet5
      about = ("I am an A I based computer program. But i can help you like you are my close friend!")
      speak(about)
      print(about+"(version 1.0)")

    elif "wikipedia" in ip.lower():                                                                                                    #wikipedia
      donot(ip)
      speak("Searching Wikipedia")
      ip=ip.replace("wikipedia","")
      results = wikipedia.summary(ip,sentences=1)
      speak(results)
      speak("Thats all in brief")

    elif (("open" in ip) or ("launch" in ip)) and (('instagram' in ip) or ("insta" in ip)):                                            #instagram
      donot(ip)
      speak("opening Insta gram")
      webbrowser.open("https://www.instagram.com")

    elif (("open" in ip) or ("launch" in ip)) and ('facebook' in ip) or ("fb" in ip):                                                  #facebook
      donot(ip)
      speak("opening facebook")
      webbrowser.open("https://www.facebook.com")

    elif (("open" in ip) or ("launch" in ip)) and ('youtube' in ip):                                                                  #youtube
      donot(ip)
      speak("opening youtube")
      webbrowser.open("https://www.youtube.com")

    elif (("search" in ip) or ("find" in ip)) and ("youtube"):                                                                        #search anythin in youtube
      donot(ip)
      speak("What has to searched in youtube ?")
      print("What has to searched in youtube ?  ",end='')
      sear=input()
      speak("Searching "+sear+" in youtube")
      os.system("start https://www.youtube.com/results?search_query="+sear)

    elif (("open" in ip) or ("launch" in ip)) and ('whatsapp' in ip):                                                                   #whatsapp
      donot(ip)
      speak("opening whatsapp")
      webbrowser.open("https://www.whatsapp.com")

    elif (("open" in ip) or ("launch" in ip)) and (('mail' in ip) or ("gmail" in ip) or ("email" in ip)):                                 #gmail
      donot(ip)
      speak("opening G mail")
      webbrowser.open("https://www.gmail.com")

    elif (("tell" in ip) or ("show" in ip)) and (('weather' in ip) or ("climate" in ip) or ("temperature" in ip)):                                 #weather
      donot(ip)
      speak("Opening M S N weather")
      os.system("start bingweather:")

    elif (("open" in ip) or ("launch" in ip)) and (('run' in ip) or ("website" in ip) or ("link" in ip) or ("webpage" in ip)):           #open any website
      donot(ip)
      speak("Provide me the U R L of the page you wish to open")
      print("Type the URL here :- ",end='')
      link=input()
      os.system("start "+link)

    elif (("show" in ip) or ("launch" in ip) or ("open" in ip)) and (('control panel' in ip) or ("control-panel" in ip)):               #control panel
      donot(ip)
      speak("opening Control Panel")
      os.system("control panel")

    elif (("show" in ip) or ("display" in ip) or ("open" in ip)) and (('processes' in ip) or ("programs" in ip)):               #show current running process
      donot(ip)
      speak("Showing all the present running tasks")
      os.system("tasklist")

    elif (("launch" in ip) or ("open" in ip)) and (('paint' in ip) or ("ms" in ip) or ("drawing board" in ip) ):                  #MS paint
      donot(ip)
      speak("opening Microsoft Paint")
      os.system("mspaint")

    elif (("show" in ip) or ("open" in ip)) and (('ipconfig' in ip) or ("ip" in ip) or ("ipaddress" in ip) ):                  #ipconfig
      donot(ip)
      speak("opening IP Configuration")
      os.system("ipconfig")

    elif (("connect" in ip) or ("check" in ip) or ("ping" in ip)) and (('server' in ip) or ("ip" in ip) or ("connectivity" in ip)):                 #ping
      donot(ip)
      speak("Provide the I P Address to ping")
      print("IP Address to ping :- ",end='')
      ipadd=input()
      speak("Pinging to "+ipadd)
      os.system("ping "+ipadd)

    elif (("launch" in ip) or ("open" in ip)) and (('camera' in ip) or ("cam" in ip)):                                                #camera
      donot(ip)
      speak("opening Camera")
      os.system("start microsoft.windows.camera:")

    elif ("launch" in ip) and (('calci' in ip) or ("calculator" in ip)):                                                         #calculator
      donot(ip)
      speak("opening calculator")
      os.system("calc")

    elif (("launch" in ip) or ("open" in ip)) and (("file-explorer" in ip) or  ("explorer" in ip)):                               #file explorere
      donot(ip)
      speak("opening File Explorer")
      os.system("explorer")

    elif (("create" in ip) or ("make" in ip)) and (('folder' in ip) or ("directory" in ip)):                                        #new secured/normal folder
      donot(ip)
      speak("Provide path to create the folder")
      print("Provide path to create the folder :- ", end='')
      drive=input()
      fld=drive.replace('\\','/')
      speak("Do you want to create a secured folder ? say yes or no.")
      print("Create a secured folder ? (y/n) :",end='')
      yn=input().lower()
      if yn=="yes" or yn=="y":
        speak("Provide name to the folder")
        print("Provide name to the folder :- ", end='')
        name=input()
        os.system("md "+name)
        speak("New secured folder created successfully")
      elif yn=="no" or yn=="n":
        speak("Provide name to the folder")
        print("Provide name to the folder :- ", end='')
        name=input()
        os.system("mkdir "+name)
        speak("New folder created successfully")
      else:
        speak("New folder created successfully")

    elif (("open" in ip) or ("show" in ip) or ("goto" in ip) or ("location" in ip)) and (('folder' in ip) or ("directory" in ip)):       #open folder
      donot(ip)
      speak("Provide Folder path to open")
      print("Provide Folder path to open :- ", end='')
      drive=input()
      speak("You are in "+drive+" Folder now")
      os.system("start "+drive)

    elif (("delete" in ip) or ("remove" in ip)) and (('folder' in ip) or ("directory" in ip)):                                #delete folder
      donot(ip)
      speak("Provide path previous to that folder")
      print("Provide path previous to that folder you wish to delete :- ", end='')
      dele=input()
      speak("Enter the folder name to delete")
      print("Enter the folder name to delete",end='')
      fldr=input()
      os.system("rd /s /q "+'"'+dele+"\\"+fldr+'"')
      speak("Folder deleted successfully.")

    elif (("connect" in ip) or ("launch" in ip) or ("open" in ip)) and (('wifi' in ip)):                                       #wifi
      donot(ip)
      speak("Showing you the lists of network profiles. Please select the device")
      wifiProfile=os.system("netsh wlan show profiles")  
      print(wifiProfile)
      print("Please select the device :- ", end='')
      select=input()
      os.system("netsh wlan connect name="+'"'+select+'"')

    elif (("show" in ip) or ("display" in ip)) and (('available' in ip) or ("networks" in ip)):                                    #available networks
      donot(ip)
      speak("Showing all the available networks")
      os.system("start ms-availablenetworks:")

    elif (("turnon" in ip) or ("switchon" in ip) or ("open" in ip)) and (('hotspot' in ip)):                                   #hotspot
      donot(ip)
      speak("Provide Hotspot name and Password")
      print("Provide hotspot name :- ",end='')
      htname=input()
      print("Provide hotspot password :- ",end='')
      htpswd=input()
      os.system("netsh wlan set hostednetwork mode=allow ssid="+htname+"key="+htpswd)
      os.system("wlan start hostednetwork")

    elif (("play" in ip) or ('sing' in ip)) and (("music" in ip) or ("song" in ip)):                                                  #songs
      donot(ip)
      speak("Hmm!  Well,  Ok")
      music_dir = 'C:/Users/Akhil/OneDrive/Desktop/Assistant'
      musics = os.listdir(music_dir)
      randsong = random.randrange(5)
      os.startfile(os.path.join(music_dir,musics[randsong]))  

    elif (("show" in ip) or ("display" in ip) or ("launch" in ip)) and  (("information" in ip) or ("system info" in ip) or ("about system" in ip)):  #system info
      donot(ip)
      speak("Showing System information")
      os.system("systeminfo")

    elif (("open" in ip) or ("show" in ip)) and  (("settings" in ip) or ("system" in ip)):                                      #settings
      donot(ip)
      speak("Opening System settings")
      os.system("start ms-settings:")

    elif (("search" in ip) or ("check" in ip)) and  (("app" in ip) or ("application" in ip)):                                      #search apk in MS store
      donot(ip)
      speak("Provide the name of the Application")
      print("Name of the application to be searched :- ",end='')
      app=input()
      os.system("start ms-"+app+":")

    elif (("exit" in ip) or ("close" in ip) or ("stop" in ip) or ("quit" in ip)  or ("abort" in ip)  or ("bye" in ip)):                #exit
      donot(ip)
      speak("Well, I'm going. Bye")
      break

    elif (("shutdown" in ip) or ("turnoff" in ip)) and  (("pc" in ip) or ("computer" in ip) or ("system" in ip)):                    #shutdown
      donot(ip)
      speak("Shutting Down.")
      os.system("shutdown -s")

    elif (("restart" in ip) or ("reopen" in ip)) and  (("pc" in ip) or ("computer" in ip) or ("system" in ip)):                    #restart
      donot(ip)
      speak("Restarting your system.")
      os.system("shutdown -r")

    elif (("logout" in ip) or ("signout" in ip)) and  (("pc" in ip) or ("computer" in ip) or ("system" in ip)):                    #logout
      donot(ip)
      speak("Shutting Down.")
      os.system("shutdown -l")

    else:
      temp = ip.replace(' ','+')                                                                                                       #google search
      geturl="https://www.google.com/search?q="    
      res_g = 'Sorry! I did not understand, but I will take you to internet to give you the best possible answer !'
      print(res_g)
      speak(res_g)
      webbrowser.open(geturl+temp) 
