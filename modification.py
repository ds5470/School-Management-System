import pymysql.cursors
conn= pymysql.connect(host="localhost",user="root",passwd="Dsharma@02"
                      ,database="school")
cursor = conn.cursor()
import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "a5f29aabc8f64ca78e30d99f2c2dc5ff", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

adno=int(input("Enter the admission no to modify"))
sql="select * from student where admno=%s"
cursor.execute(sql,adno)
for row in cursor:
            print(row)
result1 = speech_synthesizer.speak_text_async("Do you want to modify the record").get()            
ans=input("Do you want to modify the record(y/n)")
result1 = speech_synthesizer.speak_text_async("Do you want to modify the record").get()       
if ans=='y' or ans=='Y':
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
    sql="update student set sname=%s,fname=%s,mname=%s,address=%s,class_sec=%s,phno=%s,email=%s where admno=%s"
    recordTuple = (sname,fname,mname,address,clsec,phno,email,adno)
    # Execute query.
    cursor.execute(sql,recordTuple)
    conn.commit()
    result1 = speech_synthesizer.speak_text_async("Record updated successfully into student table").get()    
    print("Record updated successfully into student table")
elif ans=='n' or ans=='N':
    result1 = speech_synthesizer.speak_text_async("ok").get()
    print('ok')
result1 = speech_synthesizer.speak_text_async("Enter any key to continue").get()    
an=input("Enter any key to continue")

