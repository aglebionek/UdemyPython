#%%
# a walkthrough on how to send emails with gmail
# optional
import getpass
email = getpass.getpass('email: ')
password = getpass.getpass('insert password: ') # for gmail you need a special app password

# required
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo() # always do this directly after creating the object above
smtp_object.starttls()

smtp_object.login(email, password)
from_address = email
to_address = email
subject = "subj"
message = 'this is sent from inside of python script'
msg = 'Subject: ' + subject + '\n' +message # expected format
smtp_object.sendmail(from_addr=from_address, to_addrs=to_address, msg=msg)
# %%

