import pymysql.cursors
import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "a5f29aabc8f64ca78e30d99f2c2dc5ff", "westus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a speech synthesizer using the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)


conn= pymysql.connect(host="localhost",user="root",passwd="Dsharma@02",database="school")
cursor = conn.cursor()
result1 = speech_synthesizer.speak_text_async('enter the admission number to search').get()

adno=int(input("Enter the admission number to search"))
sql="select * from student where admno=%s"
recordTuple = (adno)
# Execute query.
cursor.execute(sql,recordTuple)
for row in cursor:
            print(row)
    # Execute query.
print("All records of the table student")
print()
print()
sql="select * from student"
cursor.execute(sql)
for row in cursor:
            print(row)
            #result = speech_synthesizer.speak_text_async(row).get()
result = speech_synthesizer.speak_text_async("Enter any key to continue").get()

an=input("Enter any key to continue")
conn.commit()
