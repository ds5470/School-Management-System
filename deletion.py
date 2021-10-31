import azure.cognitiveservices.speech as speechsdk
import pymysql.cursors
conn= pymysql.connect(host="localhost",user="root",passwd="Dsharma@02",database="school")
speech_key, service_region = "a5f29aabc8f64ca78e30d99f2c2dc5ff", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
cursor = conn.cursor()
adno=int(input("Enter the admission no to delete"))
sql="select * from student where admno=%s"
recordTuple = (adno)
# Execute query.
cursor.execute(sql,recordTuple)
for row in cursor:
            print(row)
            
result1 = speech_synthesizer.speak_text_async("Do you want to delete yes or no").get()
ans=input("Do you want to delete the record(y/n)")
if ans=='y' or ans=='Y':
    sql="delete from student where admno=%s"
    recordTuple = (adno)
    # Execute query.
    cursor.execute(sql,recordTuple)
    conn.commit()
    print("Record deleted successfully from student table")
    result1 = speech_synthesizer.speak_text_async('the record has been deleted from student table!').get()
result1 = speech_synthesizer.speak_text_async('Enter any key to continue').get()
an=input("Enter any key to continue")
