<?php
  /**
  * Requires the "PHP Email Form" library
  */ 

import os
import smtplib
from email.message import EmailMessage

# Replace contact@example.com with your real receiving email address
receiving_email_address = 'contact@example.com'

# Check if the PHP Email Form library exists
php_email_form = '../assets/vendor/php-email-form/php-email-form.php'
if os.path.exists(php_email_form):
    from php_email_form import PHP_Email_Form
else:
    sys.exit('Unable to load the "PHP Email Form" Library!')

# Create a new instance of PHP_Email_Form
contact = PHP_Email_Form()
contact.ajax = True

contact.to = receiving_email_address
contact.from_name = input('Enter your name: ')
contact.from_email = input('Enter your email: ')
contact.subject = input('Enter subject: ')

# Set up SMTP configuration
smtp_server = 'your_smtp_server'
smtp_port = 587  # Change the port if necessary
smtp_username = 'your_smtp_username'
smtp_password = 'your_smtp_password'

# Prepare the message
message = EmailMessage()
message.set_content(input('Enter your message: '))
message['From'] = contact.from_email
message['To'] = contact.to
message['Subject'] = contact.subject

# Connect to the SMTP server and send the message
with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(message)

print('Message sent successfully!')

