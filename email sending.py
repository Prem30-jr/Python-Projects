import smtplib
from email.message import EmailMessage

# Set up the message object
msg = EmailMessage()
msg["From"] = "sk7962544@gmail.com"
msg["To"] = "epremkumar24@gmail.com"
msg["CC"] = "prem3010057@gmail.com"  # Replace with the email address to CC
msg["BCC"] = "premkumar301005@gmail.com"  # Replace with the email address to BCC
msg["Subject"] = "Test Email"

# Set the email content
msg.set_content("Hello,\n\nThis is a test email from Python.")

# Connect to Gmail's SMTP server and send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('sk7962544@gmail.com', 'aocewqjxizgnkrlc')
    server.send_message(msg)
    print("Mail Sent successfully")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    server.quit()
