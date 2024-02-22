import pyttsx3
import wikipedia
from datetime import datetime,date,time



today=date.today()
td=today.strftime("%d/%m/%Y")


local_time = datetime.now()
current_time = local_time.strftime("%H:%M:%S")

voices=pyttsx3.init()
Input=input(f"\n Search Here  at {td} : ")
result=wikipedia.summary(Input,sentences=2)#change the the no of senteces which want to be written  as an output chage value of sentence
print("\nThe result at ",current_time,"of given input which is '",Input," 'are :\n")
print(result)
voices.say(result)
voices.runAndWait()
