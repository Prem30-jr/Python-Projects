# Python-Projects
Python script that sends an email using the Simple Mail Transfer Protocol (SMTP) to Gmail's SMTP server. Here's a breakdown of what the code does:

1.Import necessary modules:

*smtplib: Provides the functionality to send emails using the SMTP protocol.
*EmailMessage: A class from the email.message module used to construct email messages.
2.Set up the email message:

*The code creates an instance of EmailMessage and sets the email sender, recipient, CC (Carbon Copy), BCC (Blind Carbon Copy), and subject fields.
3.Set the email content:

*The email content is set to "Hello,\n\nThis is a test email from Python."
4.Connect to Gmail's SMTP server and send the email:

*The script connects to Gmail's SMTP server using the smtplib.SMTP function and the server address and port ("smtp.gmail.com" and 587 respectively).
*It then initiates a secure TLS connection with starttls() to encrypt the communication.
*The server.login() function is used to authenticate with the Gmail account (username: 'sk7962544@gmail.com', password: 'aocewqjxizgnkrlc').
*Finally, the server.send_message() function sends the email message, and upon success, it prints "Mail Sent successfully".
5.Exception handling:

*The script uses a try-except block to catch any exceptions that might occur during the process of sending the email.
*If there is an exception, it prints the error message.
6.Cleanup:

*The server.quit() function is called in a finally block to close the SMTP connection gracefully, whether the email was sent successfully or not
