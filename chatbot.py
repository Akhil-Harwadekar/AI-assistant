import pyttsx3
import datetime
import os
import random
import webbrowser
import wikipedia

engine = pyttsx3.init() # object creation
rate = engine.getProperty('rate')   
engine.setProperty('rate', 180)    

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)  

print('\t \t \t Welcome to Akhil\'s Program')
print('\t \t \t----------------------------')	

def greet():
    name="Akill"
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
  print(" 1) Browser \t 2) Editors \t 3) Media Players \t 4) Date \t 5) Time \t 6) Font-Colour \t 7) Wikipedia \t 8) Instagram \t 9) WhatsApp \t 10) Facebook")
  print("11) Youtube \t 12) Gmail \t 13) Control-Panel \t 14) WiFi \t 15) Songs \t 16) Create Folder \t 17) Open Folder \t 18) Python \t 19) MS-Paint \t 20) Camera")
  print("20) IP-configuration \t 21) Ping \t 22) Shut-Down")
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
      		
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("windows player" in ip) or ("windows" in ip)):           #win player
      donot(ip)
      speak("Opening Windows Media Player")
      os.system("wmplayer")
 
    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("media" in ip) or ("player" in ip) or ("vlc" in ip)):               #vlc
      donot(ip)
      speak("Opening VLC Player")
      os.system("vlc")

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("media player" in ip) or ("media" in ip) or ("player" in ip)):         #media
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

    elif (("run" in ip) or ("open" in ip) or ("launch" in ip)) and (("python" in ip) or ("prompt" in ip)):                              #python 
      donot(ip)
      speak("Opening Python Prompt")
      os.system("python")

    elif ("clear" in ip) or ("screen" in ip) or ("cls" in ip):                                                                          #clear screen 
      donot(ip)
      speak("Clearing the screen")
      os.system("cls")

    elif (("set" in ip) or ("show" in ip)) and ("date" in ip):                                                                          #date
      donot(ip)
      speak("Showing today's date")
      os.system("date")

    elif (("set" in ip) or ("show" in ip)) and (("time" in ip) or ("clock" in ip) or ("watch") in ip):                                    #time
      donot(ip)
      speak("Time is ")
      os.system("time") 

    elif (("change" in ip) or ("apply" in ip)) and (("clr" in ip) or ("color" in ip) or ("colour" in ip)):                              #color
      donot(ip)
      speak("Pick the number you would like to change your text colour to?")
      print("0-Black \t 1-Blue \t 2-Green \t 3-Aqua \t 4-Red")
      print("5-Purple \t 6-Yellow \t 7-White \t 8-Gray \t 9-Light Blue \t :- ",end='')
      bg=input()
      if int(bg) in range(10):
        os.system("color "+bg)    
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

    elif ("who are you" in ip) or ("about you" in ip) or ("your details" in ip) or ("something" in ip):                       #greet5
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

    elif (("open" in ip) or ("launch" in ip)) and ('whatsapp' in ip):                                                                   #whatsapp
      donot(ip)
      speak("opening whatsapp")
      webbrowser.open("https://www.whatsapp.com")

    elif (("open" in ip) or ("launch" in ip)) and (('mail' in ip) or ("gmail" in ip) or ("email" in ip)):                                 #gmail
      donot(ip)
      speak("opening G mail")
      webbrowser.open("https://www.gmail.com")

    elif (("show" in ip) or ("launch" in ip) or ("open" in ip)) and (('control panel' in ip) or ("control-panel" in ip)):               #control panel
      donot(ip)
      speak("opening Control Panel")
      os.system("control panel")

    elif (("launch" in ip) or ("open" in ip)) and (('paint' in ip) or ("ms" in ip) or ("drawing board" in ip) ):                  #MS paint
      donot(ip)
      speak("opening Microsoft Paint")
      os.system("mspaint")

    elif (("show" in ip) or ("open" in ip)) and (('ipconfig' in ip) or ("ip" in ip) or ("ipaddress" in ip) ):                  #ipconfig
      donot(ip)
      speak("opening IP Configuration")
      os.system("ipconfig")

    elif (("connect" in ip) or ("check" in ip) or ("ping" in ip)) and (('server' in ip) or ("connectivity" in ip)):                 #ping
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

    elif (("create" in ip) or ("make" in ip)) and (('folder' in ip) or ("directory" in ip)):                                        #new folder
      donot(ip)
      speak("Provide name to the folder")
      print("Provide name to the folder :- ", end='')
      name=input()
      os.system("mkdir "+name)
      speak("New folder ceated successfully")

    elif (("open" in ip) or ("show" in ip) or ("goto" in ip) or ("location" in ip)) and (('folder' in ip) or ("directory" in ip)):       #open folder
      donot(ip)
      speak("Provide Drive name to open")
      print("Provide Drive name to show all the folders :- ", end='')
      drive=input()
      os.system(drive+":")
      speak("You are in "+drive+" Drive now")
      os.system("start "+drive+":")

    elif (("connect" in ip) or ("launch" in ip) or ("open" in ip)) and (('wifi' in ip) or ("internet" in ip)):                        #wifi
      donot(ip)
      speak("Showing you the lists of network profiles. Please select the device")
      wifiProfile=os.system("netsh wlan show profiles")  
      print(wifiProfile)
      print("Please select the device :- ", end='')
      select=input()
      os.system("netsh wlan connect name="+'"'+select+'"')

    elif (("play" in ip) or ('sing' in ip)) and (("music" in ip) or ("song" in ip)):                                                  #songs
      donot(ip)
      speak("Hmm!  Well,  Ok")
      music_dir = 'C:/Users/Akhil/Mymusic/songs'
      musics = os.listdir(music_dir)
      randsong = random.randrange(5)
      os.startfile(os.path.join(music_dir,musics[randsong]))  

    elif (("exit" in ip) or ("close" in ip) or ("stop" in ip) or ("quit" in ip)  or ("abort" in ip)  or ("bye" in ip)):                #exit
      donot(ip)
      speak("Well, I'm going. Bye")
      break

    elif (("shutdown" in ip) or ("turnoff" in ip)) and  (("pc" in ip) or ("computer" in ip) or ("system" in ip)):                    #shutdown
      donot(ip)
      speak("Shutting Down.")
      os.system("shutdown -s")

    else:
      temp = ip.replace(' ','+')                                                                                                       #google search
      geturl="https://www.google.com/search?q="    
      res_g = 'Sorry! I did not understand, but I will take you to internet to give you the best possible answer !'
      print(res_g)
      speak(res_g)
      webbrowser.open(geturl+temp) 
