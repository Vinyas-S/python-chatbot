import pyttsx3
import os
from os import system
import time

pyttsx3.speak("welcome to the chatbot")

print("\n")

print("Hi  there , " ,end='\n ')
z=input()

if("hi" in z) or ("hello"in z) or ("helo" in z) or ("hey" in z) or ("namaste" in z ) or ("yoo" in z):
  print("Was  it  you  who  woke  me  up", end='\n ')
 
w=input()

if(("yes" in w) or ("me" in w) or ("yeah" in w) or ("yep" in w ) or ("yess" in w) or ("no" in w)):
  print("Hello,  I am  Vinny")
  pyttsx3.speak("Hello , I  am  Vinny ")

  print("Your  good  name?" ,end='\n ')

y = input()

pyttsx3.speak("Hey,     " +y )
print("How  are  you  doing " , y ,end='\n ')
x=input()

if (("hello" in x) or("hi" in x) or ("great" in x) or ("bad" in x) or ("fantastic" in x) or ("super" in x) or ("superb" in x) or ("all right" in x) or ("not bad" in x) or ("notbad" in x) or ("excited"in x) or ("well" in x) or  ("good" in x) or ("fine" in x) or ("awesome"in x)) or("sail" in x) :
 print("Wonderful,  Its  Awesome  to  help  you  anytime ", end='\n')
time.sleep(2)

while True : 
  pyttsx3.speak("please tell what do you want me to do ")
  print("can  you  please  tell  what  do  you  want  me  to  do :" , end='  ')
  p=input() 
  pyttsx3.speak("in process")

  if (("run" in p ) or ("launch" in p) or ("execute" in p) or ("open" in p) or ("start" in p)) and (("chrome" in  p) or ("browser" in p) or ("google" in p) or ("search" in p) or ("explorer" in p)) and (("do not" not in p) and ("donot" not in p) and ("dint" not in p) and ("dont" not in p) and ("don't" not in p) and ("bye" not in p) and ("not" not in p)):
   system("chrome")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done", y)

  elif (("run" in p )  or ("launch" in p) or ("open" in p) or ("start" in p) or ("execute" in p)) and (("notepad" in  p) or ("editor" in p) or ("text" in p)) and (("do not" not in p) and ("dont" not in p) and ("donot" not in p)  and ("don't" not in p) and ("dint" not in p) and ("bye" not in p)):
   system("notepad")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif (("run" in p ) or ("launch" in p) or ("open" in p) or ("start" in p) or ("execute" in p)) and (("vlc" in p) or ("video" in p) or ("windows media" in p)  or ("window media" in p) or ("player" in  p) or ("media" in p))  and (("do not" not in p) and ("dint" not in p) and ("donot" not in p)  and ("dont" not in p) and ("bye" not in p) and ("don't" not in p) and ("not" not in p)):
   system("wmplayer")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif (("run" in p) or ("execute" in p) or ("launch" in p ) or ("start" in p) or ("open" in p)) and (("painting" in p) or ("paint" in p ) or (" mspaint" in p ) or("ms paint" in p)) and (("do not" not in p) and ("dint" not in p) and ("donot" not in p) and ("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
   system("start mspaint")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif (("run" in p) or ("execute" in p) or ("open" in p ) or ("start" in p) or ("launch" in p)) and (("calci" in p ) or ("calculator" in p) or ("calc" in p)) and (("do not" not in p) and ("dint" not in p)  and ("don't" not in p) and ("donot" not in p)  and ("dont" not  in p )and ("not " not  in p )):
   system("start calc")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif (("launch" in p) or ("execute" in p) or ("open" in p )or ("start" in p) or ("run" in p)) and (("excel" in p ) or ("microsoft excel" in p ) or ("sheet" in p)) and (("do not" not in p) and ("dint" not in p) and ("don't" not in p) and ("donot" not in p)  and ("dont" not  in p )and ("not " not  in p )):
   system("start excel")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("word" in p ) or ("microsoft word" in p ) )) and (("do not" not in p) and ("dint" not in p) and ("don't" not in p) and ("donot" not in p)  and ("dont" not  in p )and ("not " not  in p )):
   system("start winword")
   pyttsx3.speak("Job  is  done "  +y)
   print(" Job  is  done",y)

  elif (("dont" in p) or ("dint" in p) or ("do not " in p) or ("donot"  in p) or  ("don't" in p) or ("not" in p)):
   pyttsx3.speak("Ok  your  wish " +y)
   print("OK,  your  wish" , y) 
   
  elif (("exit" in p) or ("quit" in p)):
   break

  else: 
   pyttsx3.speak("sorry we do not support ,")
   print("sorry  we  do  not  support")
   pyttsx3.speak("bye , call me anytime " +y)
   print("Bye,  And  call  me  any  time")
   
