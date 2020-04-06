import smtplib

smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
smtpServer.ehlo()
smtpServer.starttls()

smtpServer.login('@gmail.com', '')

subject = 'Test'
body = 'Test'
msg = f'Subject: {subject}\n\n\n {body}'

smtpServer.sendmail('iamtomgraham@gmail.com', 'iamtomgraham@gmail.com', msg)
print ('Sucessfully sent.')
smtpServer.quit()
