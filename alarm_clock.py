import time
import winsound
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("enter the time for the alarm to ring")
alarm_time=input("enter the time for the alarm to ring: (HH:MM): ")

def speak_for_alarm():
    speak(f"its the time......{current_time}")

while True:
    current_time=time.strftime("%H:%M")
    if current_time == alarm_time:
        print(f"its the time......{current_time}")
        speak_for_alarm()
        speak_for_alarm()
        speak_for_alarm()
        break


