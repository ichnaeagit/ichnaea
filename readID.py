import RPi.GPIO as GPIO
import MFRC522
import signal
import sys

def read():

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

            return ID

    
