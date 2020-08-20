import pyttsx3
import os

pyttsx3.speak("welcome")

print("\n")
print("plz chat with me what are your requirements")
print("\n")

print("enter your choice" , end=' \n')
p = input()

if ("run" in p) and (("chrome" in p) or ("google" in p)):
 os.system("chrome")

 if ("run" in p) and (("notepad" in p) or ("editor" in p)):
 os.system("notepad")

if ("run" in p) and (("wmplayer" in p) or ("player" in p))
 os.system("wmplayer")

else: 
 print("do not support")