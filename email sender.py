#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install jinja2


# In[1]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
email_address = 'your_email@gmail.com'
password = 'your_password'
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# List of recipients and their names
recipients = {
    'recipient1@example.com': 'Recipient 1',
    'recipient2@example.com': 'Recipient 2',
    # Add more recipients as needed
}

# Email content
subject = 'Personalized Email'
body = 'Hello {name},\n\nThis is a personalized email for you.\n\nBest regards,\nYour Name'

# Connect to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_address, password)

# Send personalized emails
for recipient_email, recipient_name in recipients.items():
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body_with_name = body.format(name=recipient_name)
    msg.attach(MIMEText(body_with_name, 'plain'))
    server.sendmail(email_address, recipient_email, msg.as_string())

# Close the connection to the SMTP server
server.quit()


# In[ ]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
import getpass

def send_email(subject, to_email, template, context, smtp_server, smtp_port, smtp_username, smtp_password):
    # Load the Jinja2 template
    template_loader = FileSystemLoader(searchpath=".")
    template_env = Environment(loader=template_loader)
    email_template = template_env.get_template(template)

    # Render the template with the provided context
    email_content = email_template.render(context)

    # Set up the email message
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the HTML content to the email
    message.attach(MIMEText(email_content, 'html'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())

if __name__ == "__main__":
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your.email@gmail.com"
    smtp_password = getpass.getpass("Enter your email password: ")

    # Email content
    subject = "Personalized Greeting"
    to_email = "recipient@example.com"

    # Template and context for the email
    template = "email_template.html"
    context = {
        'name': 'John Doe',
        'message': 'Hello, {{ name }}! This is a personalized email.'
    }

    # Send the email
    send_email(subject, to_email, template, context, smtp_server, smtp_port, smtp_username, smtp_password)

    print("Email sent successfully!")


# In[ ]:




