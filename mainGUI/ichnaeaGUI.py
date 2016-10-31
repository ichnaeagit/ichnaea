import Tkinter as tk    # For GUI code
import tkMessageBox     # For error boxes
import RPi.GPIO as GPIO # For using GPIO pins
import signal   # Not sure
import sys      # Used for exiting apps
import MySQLdb  # Talk to mysql database
import urllib2  # For reading websites
import MFRC522  # Used for reading ID card

continuousRun = True #Always runs

# How to quite program
def quitProgram():
        continuousRun = False
        print "Exiting"
        root.destroy()
        sys.exit()

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
        print "Ctrl+C captured, ending read."
        GPIO.cleanup()
        sys.exit()

def cardRead():

    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()
    # This loop keeps checking for chips. If one is near it will get the UID and authenticate

    # infinite read loop for ID cards
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

            ID = int(str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3]))

            # Sets default username and clock number
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
                #tkMessageBox.showwarning("header", "\n Check ethernet or if user is registered and try again.\n\nContact Teal")

            if userName:

                # Print writing successful, and ask for project input
                print "\n%s has been successfully logged in" % (userName)
                
            return userName, userClockNum

def saveinfo(ID, project, userName):

    #save username, clocknum, project, timestamp, and durration to db
    try:
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
        cursor = db.cursor()

        # get the last log for user, and find durration difference
        getTimeLogs = "SELECT logtime, nextProject FROM logs WHERE clockNum = '%d'" % (ID)
        cursor.execute(getTimeLogs)
        logtimes = cursor.fetchall()

    except:
        print "error in getting log times"
        open('logFile.txt', 'a').write("error in getting log times\n")
        db.close()

    try:
        # extract the last log of the user
        lastLog = logtimes[-1]

        # Extract the last project they logged into
        loggedProject = lastLog[-1]
        
        lastLog = str(lastLog)
        lastLog = lastLog.split()
        lastLog = [s.strip('(datetime.datetime(') for s in lastLog]
        lastLog = [s.strip('),)') for s in lastLog]

        # gets current time from a website (notice: must adjust hour by 4!)
        pageURL = urllib2.urlopen("http://just-the-time.appspot.com")
        timeDate = pageURL.read()

        timeDate = timeDate.replace('-',' ')
        timeDate = timeDate.replace(':',' ')
        time = timeDate.split()
        open('logFile.txt', 'a').write("Time now:")
        for unit in time:
            open('logFile.txt', 'a').write(unit+",")
        open('logFile.txt', 'a').write("\n")
        
        # store time differences
        #sometimes sec diff is zero or isn't there so fixes it
        try:
            secDiff = float(time[5]) - float(lastLog[5])
        except:
            secDiff = 0
        
        minDiff = float(time[4]) - float(lastLog[4])
        hourDiff = (float(time[3])-5) - float(lastLog[3])
        dayDiff = float(time[2]) - float(lastLog[2])
        monthDiff = float(time[1]) - float(lastLog[1])
        yearDiff = float(time[0]) - float(lastLog[0])

        open('logFile.txt', 'a').write("Time last log:")
        for x in range(0,5):
                open('logFile.txt', 'a').write(lastLog[x]+",")
        open('logFile.txt', 'a').write("\n")
       
        # set minute differences
        timeDiffMin = (hourDiff * 60) + minDiff + (secDiff / 60)

        #print timeDiffMin
        info = str(timeDiffMin)
        info = "Unaltered time diff: " + info + " min\n"
        open('logFile.txt', 'a').write(info)

        if timeDiffMin < 0 : #and dayDiff = 0:
                print "Error in time difference"
                open('logFile.txt', 'a').write("Error in time difference\n")
                timeDiffMin = 0

        # if someone clocks on for over 360min, then count only as 360 min
        if timeDiffMin > (360):
            timeDiffMin = 360
            print "time diff too long"
            open('logFile.txt', 'a').write("Time diff too long\n")

        # make sure to not count time off
        if loggedProject == "Clock Off":
            timeDiffMin = 0
        
        db.close()

    except:
        print "Error in time calc"
        open('logFile.txt', 'a').write("Error in time calc or first log")
        tkMessageBox.showwarning("header", "Error regarding time durration.\n OR this is your first log. \n\nContact Teal")
        timeDiffMin = 0
        loggedProject = "N/A"

    # print new project, and previous project
    try:
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
        cursor = db.cursor()
        
        values = (ID, project,loggedProject, timeDiffMin, userName)
        addTime = "INSERT INTO logs (clockNum, nextProject, loggedProject, logdurr, userName)" \
                  "VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(addTime, values)
        db.commit()
        db.close()
        info = "%s commited to db\n" % userName
        print info
        open('logFile.txt', 'a').write(info)

    except:
        print "error writing to db"
        open('logFile.txt', 'a').write("Error writing to db\n")
        tkMessageBox.showwarning("header", "Error writing to db. \n\nContact Teal")
        db.rollback()
        db.close()

    open('logFile.txt', 'a').write("\n")
    root.destroy()

def buttonPressed():
    print 'Please scan your card'
    projects = []
    project = int(0)

    # Run program to scan card info to file
    name, ID = cardRead()
    userName = 'Hello '
    userName +=name

    # Prints names
    nameLabel =tk.Label(root, text=userName, font=("Helvetica",18))
    nameLabel.grid()
    helpText = tk.Label(root, text='Please pick a project', fg="blue")
    helpText.grid()

    #Get project names
    try:
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
        cursor = db.cursor()
        projectSearch = "SELECT * FROM users WHERE clocknum = '%d'" % (ID)
        # does the thing
        cursor.execute(projectSearch)
        # fetch the username as a string
        projects = cursor.fetchone()
        db.close()
    except:
        print "Getting projects failed. User not registered (or connection issue)"
        open('logFile.txt', 'a').write("Getting projects failed. User not registered (or connection issue)\n")
        tkMessageBox.showwarning("header", "User not registered\nContact Teal")
        root.destroy()
        return

    # Sets pad size depending on how many projects
    padSize = 20
    if projects[7]: padSize = 10
    if projects[10]: padSize = 2
    
    # Create buttons
    projects = projects[4:]    
    # For each valid project
    # i is index, for color changing
    for i, project in enumerate(projects):

        project = str(project) # changes the project to a string

        if project == "None": break # breaks if no project

        # Create button with given label, and alternate colors
        # pad size changes from above
        # project = project saves the specific instance of project to the given button
        tk.Button(root,text = project, \
            bg= ("RoyalBlue1" if i % 2 else "turquoise4"),  command=lambda project = project: \
            saveinfo(ID,project,name),  \
            width = '20', height=1, font = ("Helvetica", 24)) \
            .grid(pady=padSize)

    # Creates clock off button
    tk.Button(root,text='Clock Off', bg="red", command=lambda: \
        saveinfo(ID,"Clock Off",name), width = '20', \
        height=1, font = ("Helvetica", 24)). \
        grid(pady=padSize)

# Continuously runs main app
while continuousRun:

    class MainApplication(tk.Frame):
        def __init__(self,parent, *args, **kwargs):
            tk.Frame.__init__(self,parent, *args, **kwargs)
            self.parent = parent
            root.geometry('475x750+0+0') # Sets size of app

            scanCard = tk.Label(root, text="Please Scan Card", font=("papyrus",30), fg="red", width=20)
            scanCard.grid(pady=10)

            # auto starts code after generating the GUI
            root.after(500, buttonPressed)

   # Allows to run as main or as a function
    if __name__ == "__main__":

        root = tk.Tk()
        root.title("Ichnaea time tracking")
        display = MainApplication(root)
        root.mainloop()
