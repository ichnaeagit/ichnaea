#!/usr/bin/env python
# -*- coding: utf8 -*-


import numpy as np
import RPi.GPIO as GPIO
import MFRC522
import signal
import sys
import datetime
import time
from time import gmtime, strftime
from datetime import datetime
from Tkinter import *
import MySQLdb



def readAndSave():
        
    continue_reading = True

    ## Name database
    with open('IDnames') as f:
        IDnames = f.read().splitlines()
    with open('IDnumbers') as f:
        IDs = f.read().splitlines()
    IDnumbers = map(int, IDs)
    
    #IDnames = ['Teal',      'Troy',     'Mat']
    #IDnumbers = [22011113197,1981523126, 22011113190]

    # Capture SIGINT for cleanup when the script is aborted
    def end_read(signal,frame):
        global continue_reading
        print "Ctrl+C captured, ending read."
        continue_reading = False
        GPIO.cleanup()
        sys.exit()
        

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    # Welcome message
    #print "Welcome to the MFRC522 data read example"
    #print "Press Ctrl-C to stop."
      # This loop keeps checking for chips. If one is near it will get the UID and authenticate

    while continue_reading:
         # Show message
        
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
      
            if ID in IDnumbers:

                # get current time
                date_time = str(datetime.now())

                # Find name from list
                tempNameLocal = IDnumbers.index(ID)
                tempName = IDnames[tempNameLocal]

                # Write username and time to end of file
                with open('outputFile.txt','a') as outputFile:
                    outputFile.write("\nUsername,%s,ID,%d," % (tempName, ID))
                    outputFile.write("Login,%s," % date_time)

                # Print writing successful, and ask for project input
                print "\n%s has been successfully logged in" % (tempName)

                #pickProject.pick()


                continue_reading = False
                outputFile.close()
                
                return tempName, ID

            # If unknown ID number, then   
            else:
                with open('outputFile.txt','a') as outputFile:
                    outputFile.write("\nUser unknowon. ID,%s" % ID)
                print "Unknown user\n\n Ready to scan again"
                

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
                
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                 MIFAREReader.MFRC522_Read(8)
                 MIFAREReader.MFRC522_StopCrypto1()
            #else:
                #print "Authentication error"

    #### close file
    outputFile.close()
    GPIO.cleanup()

