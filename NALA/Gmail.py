

from datetime import date
import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from mimetypes import guess_type as guess_mime_type
from NALA import Speech







# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
your_email = "jarvisassistant50@gmail.com"


def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    with open("A:\py programs//NALA//token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("C:\\Users\\arsha\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\google_auth_oauthlib\\gmailAPI.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("A:\py programs//NALA\\token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
try:
    service = gmail_authenticate()
except Exception as e :
    print(e)

def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

def build_message(destination, obj, body, attachments=[]):
    if not attachments: # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = your_email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = your_email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body, attachments)
    ).execute()
'''    
try:
    # test send email
    send_message(service, "masshero97@gmail.com", "This is a subject", 
                "This is the body of the email",["test.txt", "anyfile.png"])
    print("Sent successfully!")            
except:
    print("Failed !!")    
'''
def check_mails(service):
	
	# fetching emails of today's date
	today = (date.today())

	today_main = today.strftime('%Y/%m/%d')

	# Call the Gmail API
	results = service.users().messages().list(userId = 'me',
											labelIds=["INBOX","UNREAD"],
											q="after:{0} and category:Primary".format(today_main)).execute()
	# The above code will get emails from primary
	# inbox which are unread
	messages = results.get('messages',[])


	if not messages:
			
		# if no new emails
		print('No messages found.')
		Speech.speak('No messages found.')
	else:
		m=""
		
		# if email found
		Speech.speak("{} new emails found".format(len(messages)))

		Speech.speak("if you want to read any particular email just type read ")
		Speech.speak("and for not reading type leave ")
		for message in messages:

			msg=service.users().messages().get(userId='me',
											id = message['id'], format = 'metadata').execute()

			for add in msg['payload']['headers']:
				if add['name']=="From":

					# fetching sender's email name
					a=str(add['value'].split("<")[0])
					print(a)

					Speech.speak("email from"+a)
					text=input()

					if text == "read":

						print(msg['snippet'])
						
						# speak up the mail
						Speech.speak(msg['snippet'])
#check_mails(service)