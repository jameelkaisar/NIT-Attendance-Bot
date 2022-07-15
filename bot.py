from os import environ
from pyrogram import Client, filters, enums
import pytesseract
try:
  from PIL import Image
except ImportError:
  import Image
from gtts import gTTS
import re
from datetime import datetime

def nitAttendance(message, srcImg, srcTxt, srcMP3):
  
  returnArray = []
  stdNames = ['Jameel Kaisar Khan', 'Saqib Hussain Ganaie', 'Irtiqa', 'Arpunit Kour', 'Mandeep Singh', 'Pranav Sanotra', 'Uday Bhan', 'Rohit Singh', 'Akarshit Kumar', 'Gaurav Meena', 'Shagun Bhatt', 'Zeeshan Sharif', 'Ishita Sharma', 'Aabid Mushtaq', 'Shaik Arsh Husssain', 'Astitva Mishra', 'Rahul', 'Hardik Srivastava', 'Vishal Tyagi', 'Ashish Kumar', 'Devansh', 'Parath Safaya', 'Hemanshu Sharma', 'Saliq Gowhar Khan', 'Mridul Sharma', 'Shreya', 'Ketan Sharma', 'Fasil Shafi', 'Agrim Sangotra', 'Ankita Rajput', 'Rishita Sharma', 'Haseeb Hijazi Khan', 'Dhananjay Mahajan', 'Adnan Ali Ganaie', 'Ravishta Kohli', 'Japsimar Soin', 'Syeda Azhar Fatimah', 'Sadiya Ajaz Churoo', 'Shahzareena', 'Adarsh Kumar', 'Abhay Garg', 'Sarveshwara Mishra', 'Aryan Patel', 'Rituraj Kumar Singh', 'Gade Venkata Kasi Sunil', 'Aditya Gupta', 'Harsh Raj', 'Harshit Dubey', 'Usaid Aijaz', 'Yasir Mohi Ud Din', 'Deepak Kachhot', 'Rohit Prajapat', 'Rahul Singh', 'Dokiburra Isaiah Paulson', 'Srinath Rakesh Yatawar', 'Kundan Kumar Yadav', 'Dinesh Dhidhariya', 'Ankit Kumar', 'Yachalapu Lova Sai Prasanth', 'Lanka Koushik', 'Stuti Singh', 'Guruju Akhila', 'Ismail Bashir', 'Shivam Singh Khatri', 'Zahoor Ahmad Shergujry', 'Shahid Mushtaq', 'Rayees Zahoor', 'Abhishiek', 'Kundan Kumar', 'Bhagat Snehankit Narendra', 'Rahul Kumar', 'Udayveer Singh', 'Mousumi Biswas', 'Sonia', 'Sommit Thappa', 'Tania', 'Vikram Digra', 'Akanksha Kumari', 'Goutam Mech', 'Rathlavath Ganesh', 'Zeeshan Arif', 'Rishav Hodoker', 'Phuntsog Namgyal', 'Muzaffar Ali', 'Moin Bashir Zargar', 'Kajal Kumari']
  stdAbs = []
  stdPre = []
  stdTxt = ""
  stdAtt = ""

  tempMsg = app.send_message(chat_id=message.from_user.id, text="Processing Image...", disable_notification=True)
  try:
    stdImg = Image.open(srcImg)
#    app.send_message(chat_id=message.from_user.id, text="**Image Data:**\n" + str(stdImg))
  except Exception as err:
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
    app.send_message(chat_id=message.from_user.id, text="Unable to Process Image\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\n__Please Resend the Image__")
    return
  app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
  
  tempMsg = app.send_message(chat_id=message.from_user.id, text="Recognizing Image Text...", disable_notification=True)
  try:
    pytesseract.pytesseract.tesseract_cmd = r"/app/.apt/usr/bin/tesseract"
  except:
    pass
  try:
    imgTxt = pytesseract.image_to_string(stdImg)
#    imgTxt = "2020dehf2020b$$ItE#  0@#$ .%011hgfgd66"
  except Exception as err:
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
    app.send_message(chat_id=message.from_user.id, text="Unable to Recognize Image Text\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\n__Please Resend the Image__")
    return
  app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
  
  tempMsg = app.send_message(chat_id=message.from_user.id, text="Processing Image Text...", disable_notification=True)
  imgString = re.sub('[^A-Za-z0-9]+', '', imgTxt)
  for i in range(0, 86):
    stdRoll = "2020BITE"+str(i+1).zfill(3)
    if (imgString.upper().find(stdRoll) != -1):
      rollRes = "✅  [2020BITE" + str(i+1).zfill(3) + "]  " + stdNames[i].split()[0]
      stdAtt = stdAtt + "\n" + rollRes
      stdPre.append(i)
    else:
      rollRes = "❌  [2020BITE" + str(i+1).zfill(3) + "]  " + stdNames[i].split()[0]
      stdAtt = stdAtt + "\n" + rollRes
      stdAbs.append(i)
  stdTxt = stdTxt + "Total Number of Students: " + str(len(stdNames))
  stdTxt = stdTxt + "\nAttendees: " + str(len(stdPre))
  stdTxt = stdTxt + "\nAbsentees: " + str(len(stdAbs))
  stdTxt = stdTxt + "\n\nList of Students:\n"
  stdTxt = stdTxt + stdAtt
  returnArray.append(stdTxt)
  app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
  
  tempMsg = app.send_message(chat_id=message.from_user.id, text="Creating Text Report...", disable_notification=True)
  try:
    with open(srcTxt, mode ='w') as file:
      file.write(stdTxt)
    returnArray.append(str(1))
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
  except Exception as err:
    returnArray.append(str(0))
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
    app.send_message(chat_id=message.from_user.id, text="Failed to Create Text Report\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\n__Text Report won't be sent__")
  
  tempMsg = app.send_message(chat_id=message.from_user.id, text="Creating Audio Report...", disable_notification=True)
  sound0 = "Attendance Report of " + datetime.today().strftime("%B %d, %Y") + "."
  sound1 = str(len(stdPre)) + " out of 86 students were present in the class. " + ("No", str(len(stdAbs)))[len(stdAbs)>0] + " student" + (" was", "s were")[len(stdAbs)>1] + " absent."
  sound2 = ""
  sound3 = "Name of student" + (" who was", "s who were")[len(stdPre)>1] + " present in the class."
  sound4 = "Name of student" + (" who was", "s who were")[len(stdAbs)>1] + " absent in the class."
  try:
    with open(srcMP3, 'wb') as f:
      gTTS(sound0, lang='en').write_to_fp(f)
      gTTS(sound1, lang='en').write_to_fp(f)
#      gTTS(sound2, lang='en').write_to_fp(f)
      if (len(stdPre)>0):
        gTTS(sound3, lang='en').write_to_fp(f)
        for i in stdPre:
          if (len(stdPre)>1 and i==(stdPre[len(stdPre)-1])):
            gTTS("and", lang='en').write_to_fp(f)
          gTTS("Roll Number " + str(i+1), lang='en').write_to_fp(f)
          gTTS(stdNames[i], lang='ur').write_to_fp(f)
      if (len(stdAbs)>0):
        gTTS(sound4, lang='en').write_to_fp(f)
        for i in stdAbs:
          if (len(stdAbs)>1 and i==(stdAbs[len(stdAbs)-1])):
            gTTS("and", lang='en').write_to_fp(f)
          gTTS("Roll Number " + str(i+1), lang='en').write_to_fp(f)
          gTTS(stdNames[i], lang='ur').write_to_fp(f)
    returnArray.append(str(1))
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
  except Exception as err:
    returnArray.append(str(0))
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
    app.send_message(chat_id=message.from_user.id, text="Unable to Create Audio Report\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\n__Audio Report won't be sent__")
  
  return returnArray

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

dep = Client(":memory:", api_id, api_hash, bot_token=bot_token)
with dep:
  dep.send_message(chat_id=977782841, text="Bot Deployed Successfully!")

app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

srcImg = ""
srcTxt = "/app/downloads/Attendance.txt"
srcMP3 = "/app/downloads/Attendance.mp3"

@app.on_message(filters.command("start"))
def welcome(client, message):
  app.send_message(chat_id=message.from_user.id, text="Hi "+ message.from_user.first_name + "!\nWelcome to NIT Attendance Bot!")
  app.send_message(chat_id=message.from_user.id, text="Send Attendance Screenshot as Document")

@app.on_message(filters.document)
def documentInput(client, message):
  if (message.document.mime_type.find("image") != -1):
    tempMsg = app.send_message(chat_id=message.from_user.id, text="Downloading Image...", disable_notification=True)
    try:
      srcImg = app.download_media(message)
    except Exception as err:
      app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
      app.send_message(chat_id=message.from_user.id, text="Unable to Download Image\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\n__Please Resend the Image__", reply_to_message_id=message.id)
      return
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.id)
    returnAttendance = nitAttendance(message, srcImg, srcTxt, srcMP3)
    if (returnAttendance==None):
      return
    myMsg = app.send_message(chat_id=message.from_user.id, text=returnAttendance[0], reply_to_message_id=message.id)
    if (returnAttendance[1]==str(1)):
      app.send_chat_action(chat_id=message.from_user.id, action=enums.ChatAction.UPLOAD_DOCUMENT)
      app.send_document(chat_id=message.from_user.id, document=srcTxt, caption="Text Report", reply_to_message_id=myMsg.id)
    if (returnAttendance[2]==str(1)):
      app.send_chat_action(chat_id=message.from_user.id, action=enums.ChatAction.UPLOAD_AUDIO)
      app.send_audio(chat_id=message.from_user.id, audio=srcMP3, caption="Audio Report", reply_to_message_id=myMsg.id)
    app.send_message(chat_id=message.from_user.id, text="Thanks for using this Bot!\n\nThis Bot is created by **[Jameel Kaisar](tg://user?id=977782841)** (__**Ajmi**__).")
  else:
    app.send_message(chat_id=message.from_user.id, text="This is not a Valid Image!", reply_to_message_id=message.id)
    app.send_message(chat_id=message.from_user.id, text="Please send a Valid Image")

@app.on_message(filters.photo)
def photoInput(client, message):
  app.send_message(chat_id=message.from_user.id, text="This is a Low Quality Image!", reply_to_message_id=message.id)
  app.send_message(chat_id=message.from_user.id, text="Please try sending this Image as Document")

@app.on_message(filters.all)
def incorrectInput(client, message):
  app.send_message(chat_id=message.from_user.id, text="Incorrect Input!", reply_to_message_id=message.id)
  app.send_message(chat_id=message.from_user.id, text="Send Attendance Screenshot as Document")

app.run()
