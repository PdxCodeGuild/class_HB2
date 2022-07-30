
import requests
from pywhatkit import send_mail 
from important import google_p


def get_response():
    response = requests.get('https://api.spaceflightnewsapi.net/v3/articles')
    return response

title_list = []
url = []
response = get_response()
json_response = response.json()  
# print(json_response)
for i in range(len(json_response)):
    spaceflight_title = json_response[i]['title']
    spaceflight_url = json_response[i]['url']
   

    title_list.append(spaceflight_title)
    url.append(spaceflight_url)
   
email_msg = []
for i in range(len(url)):
    email_msg.append(f"{title_list[i]}\n{url[i]}\n")# combining both list
 
url = '\n'.join(email_msg)# entire list and joining them in new lines in one string

# message = 
# for i in range(len(title_list)):
# print(url)


send_mail(
email_sender = 'robleroandy99@gmail.com',
email_receiver = 'aroblero@myyahoo.com',
message = f'{url}', 
password = google_p['password'],
subject = 'notification Mail'
 ) 

# print('lets see')

# sender = 'andygarcia16@yahoo.com'
# receivers = ['andygarcia22212@gmail.com']


# message = '''from: andygarcia16@yahoo.com
# to: andygarcia22212@gmail.com
# subject: STMP e-mail test message.
# '''

# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)         
#    print("Successfully sent email")
# except smtplib.SMTPException:
#     print("Error: unable to send email")



# smtp_server = "smtp.gmail.com"
# port = 587  # For starttls
# sender_email = "robleroandy99@gmail.com"
# password = input("Type your password and press enter: ")

# # Create a secure SSL context
# context = ssl.create_default_context()

# # Try to log in to server and send email
# try:
#     server = smtplib.SMTP(smtp_server,port)
#     # server.ehlo() # Can be omitted
#     server.starttls(context=context) # Secure the connection
#     server.ehlo() # Can be omitted
#     server.login(sender_email, password)
#     # TODO: Send email here
# except Exception as e:
#     # Print any error messages to stdout
#     print(e)
# finally:
#     server.quit() 
# json_response_dict = json_response[0]
# print('first response : ',  json_response_dict)
# title = json_response_dict['title']
# print('title: ', title)