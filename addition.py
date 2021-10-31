#addition of records
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "a5f29aabc8f64ca78e30d99f2c2dc5ff", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

'''speech to text'''
speech_recognizer=speechsdk.SpeechRecognizer(speech_config=speech_config)

import pymysql.cursors
conn= pymysql.connect(host="localhost",user="root",passwd="Dsharma@02",database="school")
cursor = conn.cursor()
print("Speak the admission number....")
result=speech_recognizer.recognize_once()
print("Recognized:{}".format(result.text))
result1 = speech_synthesizer.speak_text_async("You have entered admission number as"+result.text).get()
adno=result.text
print("Your Admission Number is ",adno)
sname=input("Enter the name of the student")
fname=input("Enter the father's name")
mname=input("Enter the mother's name")
address=input("Enter the address")
clsec=input("Enter class and sec")
while(1):
    phno=input("Enter the phno")
    if len(phno)==10:
        break
    else:
        print("Invalid phno")
        #print("Enter the phno again")
while(1):
    email=input("Enter the email id")
    if "@" in email:
        break
    else:
        print("Invalid email id")
        #print("Enter the email-id again") 

sql="insert into student(admno,sname,fname,mname,address,class_sec,phno,email) values(%s,%s,%s,%s,%s,%s,%s,%s)"
recordTuple = (adno, sname,fname,mname,address,clsec,phno,email)
# Execute query.
cursor.execute(sql,recordTuple)
conn.commit()
result1 = speech_synthesizer.speak_text_async("Record inserted successfully into student table").get()
result1 = speech_synthesizer.speak_text_async("Enter any key to continue").get()
print("Record inserted successfully into student table")

an=input("Enter any key to continue")


