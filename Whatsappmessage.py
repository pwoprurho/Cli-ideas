"""
Aurthor: Akpojotor Oghenerurho
Email: akporurho@proton.me
Date: 13/01/15
cli implementation of the whatsapp messanger
"""

import pywhatkit as kit
import datetime as dt
now = dt.dateime.now()
phone_number = input("Enter the recipient phone number here: ")
kit.sendwhatmsg(phone_number, message, now.hour, now.minute+1)
print("message sent successfully.")
