import imaplib
import base64
import os
import email

email_user = input('anujms@iitk.ac.in')
email_pass = input('amn52129')

mail=imaplib.IMAP4_SSL('imap.nwm.iitk.ac.in')
mail.login(email_user, email_pass)
mail.select('Subhra Sankar')



