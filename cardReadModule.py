#!/usr/bin/env python
# -*- coding: utf8 -*-


import numpy as np
import RPi.GPIO as GPIO
import MFRC522
import signal
import sys
from Tkinter import *
import MySQLdb

def readAndSave():

    # Capture SIGINT for cleanup when the script is aborted
    def end_read(signal,frame):
        print "Ctrl+C captured, ending read."
        GPIO.cleanup()
        sys.exit()

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
      # This loop keeps checking for chips. If one is near it will get the UID and authenticate

    # infinite read loop
    while True:
        
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
         # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            var1 = str(uid[0])
            var2 = str(uid[1])
            var3 = str(uid[2])
            var4 = str(uid[3])
            ID = int(var1 + var2 + var3 + var4)

            # check db for id
            db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

            cursor = db.cursor()

            sql = "SELECT username FROM users WHERE rfidnum = '%d'" % (ID)

            try:
                # does the thing
                cursor.execute(sql)
                # fetch the username as a string
                results = str(cursor.fetchone())
                # cuts the ends by 2 and 3 respectivily to take off random trash
                userName = results[2:-3]
            except:
                print "Error finding user"
            # close db
            db.close()
      
            if userName:

                # Print writing successful, and ask for project input
                print "\n%s has been successfully logged in" % (userName)
                
                return userName, ID

            # If unknown ID number, then   
            else:
                print "Unkown id"

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                
            # Select the scanned tag
            #MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                 MIFAREReader.MFRC522_Read(8)
                 MIFAREReader.MFRC522_StopCrypto1()

    #### close file
    outputFile.close()
    GPIO.cleanup()

