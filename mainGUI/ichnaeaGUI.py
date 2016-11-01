import Tkinter as tk
import tkMessageBox
import cardReadModule as cardRead
import sys
import MySQLdb
import time
import readID
from time import gmtime, strftime
import datetime
import urllib2

continuousRun = True

def quitProgram():
        continuousRun = False
        root.destroy()
        sys.exit()

        
def saveinfo(ID, project):

    #save username, clocknum, project, timestamp, and durration to db
    try:
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
        cursor = db.cursor()

        # get the last log for user, and find durration difference
        getTimeLogs = "SELECT logtime, nextProject FROM logs WHERE clockNum = '%d'" % (ID)
        cursor.execute(getTimeLogs)
        logtimes = cursor.fetchall()

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

        #print lastLog
        #print time
        
        # store time differences
        #sometimes sec diff is zero or isn't there so fixes it
        try:
                secDiff = float(time[5]) - float(lastLog[5])
        except:
                secDiff = 0
        
        minDiff = float(time[4]) - float(lastLog[4])
        hourDiff = (float(time[3])-4) - float(lastLog[3])
        dayDiff = float(time[2]) - float(lastLog[2])
        monthDiff = float(time[1]) - float(lastLog[1])
        yearDiff = float(time[0]) - float(lastLog[0])
       
        # set minute differences
        timeDiffMin = (hourDiff * 60) + minDiff + (secDiff / 60)

        print timeDiffMin

        if timeDiffMin < 0:
                print "Error in time difference"
                timeDiffMin = 0

        # if someone clocks on for over 360min, then count only as 360 min
        if timeDiffMin > (360):
            timeDiffMin = 360
            print "time diff too long"

        # make sure to not count time off
        if loggedProject == "Clock Off":
            timeDiffMin = 0
        
        db.close()
    except:
        print "error!"
        tkMessageBox.showwarning("header", "Error regarding time durration. \n\nContact Teal")
        timeDiffMin = 0
        loggedProject = "N/A"
        db.close()

    # print new project, and previous project
    try:

        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
        cursor = db.cursor()
        
        values = (ID, project,loggedProject, timeDiffMin)
        addTime = "INSERT INTO logs (clockNum, nextProject, loggedProject, logdurr)" \
                  "VALUES (%s,%s,%s,%s)"
        cursor.execute(addTime, values)
        db.commit()
        db.close()
        print "commited to db"

    except:
        
        print "error writing to db"
        tkMessageBox.showwarning("header", "Error writing to db. \n\nContact Teal")
        db.rollback()
        db.close()

    root.destroy()

def buttonPressed():
    print 'Please scan your card'
    project = int()
    project = 0

    # Run program to scan card info to file
    name, ID = cardRead.readAndSave()
    # ID2 = readID.read()

    # Only runs rest of code if there is a valid ID optained
    if ID != "None":
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
            print "Getting projects failed"
            tkMessageBox.showwarning("header", "Failed to connect to database.\n Check ethernet cord, then try again. \n\nContact Teal")



        # Prints whichever projects people have, if they have them
        button01 = tk.Button(root,text = projects[4], bg="RoyalBlue1",        command=lambda: saveinfo(ID,projects[4]),  width = '20', height=1, font = ("Helvetica", 24))
        button01.grid(pady=2)
        if projects[5]:
            button02 = tk.Button(root,text=projects[5], bg="turquoise4",      command=lambda: saveinfo(ID,projects[5]),  width = '20', height=1, font = ("Helvetica", 24))
            button02.grid(pady=2)
        if projects[6]:
            button03 = tk.Button(root,text=projects[6], bg="seagreen",      command=lambda: saveinfo(ID,projects[6]),  width = '20', height=1, font = ("Helvetica", 24))
            button03.grid(pady=2)
        if projects[7]:
            button04 = tk.Button(root,text=projects[7], bg="RoyalBlue1",      command=lambda: saveinfo(ID,projects[7]),  width = '20', height=1, font = ("Helvetica", 24))
            button04.grid(pady=2)
        if projects[8]:
            button05 = tk.Button(root,text=projects[8], bg="turquoise4",      command=lambda: saveinfo(ID,projects[8]),  width = '20', height=1, font = ("Helvetica", 24))
            button05.grid(pady=2)
        if projects[9]:
            button06 = tk.Button(root,text=projects[9], bg="seagreen",     command=lambda: saveinfo(ID,projects[9]),  width = '20', height=1, font = ("Helvetica", 24))
            button06.grid(pady=2)
        if projects[10]:
            button07 = tk.Button(root,text=projects[10], bg="RoyalBlue1",     command=lambda: saveinfo(ID,projects[10]), width = '20', height=1, font = ("Helvetica", 24))
            button07.grid(pady=2)
        if projects[11]:
            button08 = tk.Button(root,text=projects[11], bg="turquoise4",     command=lambda: saveinfo(ID,projects[11]), width = '20', height=1, font = ("Helvetica", 24))
            button08.grid(pady=2)
        if projects[12]:
            button09 = tk.Button(root,text=projects[12], bg="seagreen",    command=lambda: saveinfo(ID,projects[12]), width = '20', height=1, font = ("Helvetica", 24))
            button09.grid(pady=2)
        if projects[13]:
            button10 = tk.Button(root,text=projects[13], bg="turquoise1",     command=lambda: saveinfo(ID,projects[13]), width = '20', height=1, font = ("Helvetica", 24))
            button10.grid(pady=2)           
        button10 = tk.Button(root,text='Clock Off', bg="red", command=lambda: saveinfo(ID,"Clock Off"), width = '20',height=1, font = ("Helvetica", 24))
        button10.grid(pady=2)
    else: root.destroy()

while continuousRun:

    class MainApplication(tk.Frame):
        def __init__(self,parent, *args, **kwargs):
            tk.Frame.__init__(self,parent, *args, **kwargs)
            self.parent = parent
            root.geometry('475x750+0+0')
            #main GUI here


            #quitButton = tk.Button(root, text='Quit program', bg="red", fg ="black",height=1,width=65,font=("Helvetica",9), command = quitProgram)
            #quitButton.grid()

            #scanButton = tk.Button(root,text='Click here to scan', bg="red", fg="white", height = 3, font=("Helvetica",16), command = buttonPressed)
            #scanButton.pack(padx=5, pady=4)

            scanCard = tk.Label(root, text="Please Scan Card", font=("papyrus",30), fg="red", width=20)
            scanCard.grid(pady=10)
            
            #feedbackLabel = tk.Label(root, textvariable=helpText, fg="blue")
            #feedbackLabel.grid()
            
            root.after(500, buttonPressed)

    if __name__ == "__main__":
        root = tk.Tk()
        root.title("Ichnaea time tracking")
        #MainApplication(root).pack(side="top",fill="both",expand=True)
        display = MainApplication(root)
        root.mainloop()


   



