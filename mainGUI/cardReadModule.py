#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import sys
import MySQLdb
import tkMessageBox

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

            userName = 'failed db connect'
            userClockNum = 00000
            
            try:
                # check db for id
                db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

                cursor = db.cursor()

                userNameSearch = "SELECT username FROM users WHERE rfidnum = '%d'" % (ID)
                clockNumSearch = "SELECT clocknum FROM users WHERE rfidnum = '%d'" % (ID)

                # does the thing
                cursor.execute(userNameSearch)
                # fetch the username as a string
                userName = str(cursor.fetchone())
                # cuts the ends by 2 and 3 respectivily to take off random trash
                userName = userName[2:-3]
                
                cursor.execute(clockNumSearch)
                userClockNum = str(cursor.fetchone())
                userClockNum = int(userClockNum[1:-3])
                db.close()
            except:
                print "Error finding user"
                tkMessageBox.showwarning("header", "Failed to write to database. \n Check ethernet or if user is registered and try again.\n\nContact Teal")

            if userClockNum:

                # Print writing successful, and ask for project input
                print "\n%s has been successfully logged in" % (userName)
                
            return userName, userClockNum

    
