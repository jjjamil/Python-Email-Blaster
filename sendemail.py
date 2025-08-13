import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


smtp_server = 'smtp.gmail.com' 
smtp_port = 587                  


sender_email = 'youremail@gmail.com'
sender_password = 'yourapppassword'


def read_emails(file_path):
    email_data = []
    if file_path.endswith('.csv'):
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) >= 2:
                    email_data.append({
                        'email': row[0].strip(),
                        'name': row[1].strip()
                    })
    return email_data



email_file_path = 'emails.csv'
email_data = read_emails(email_file_path)


html_template = """
# define your html here, this will be the body of te email


"""


server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(sender_email, sender_password)


for data in email_data:
   recipient = data['email']
   name = data['name']


   html_content = html_template.format(name=name)


   msg = MIMEMultipart()
   msg['From'] = sender_email
   msg['To'] = recipient
   msg['Subject'] = "Your email subject"


   msg.attach(MIMEText(html_content, 'html'))


   server.send_message(msg)


server.quit()


print("Emails sent successfully!")