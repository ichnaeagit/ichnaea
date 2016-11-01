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
        for unit in time:
            open('logFile.txt', 'a').write(unit+",")
        
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

        #print timeDiffMin

        if timeDiffMin < 0:
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
        tkMessageBox.showwarning("header", "Error regarding time durration. \n\nContact Teal")
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
        info = "\n%s commited to db\n" % userName
        print info
        open('logFile.txt', 'a').write(info)

    except:
        print "error writing to db"
        open('logFile.txt', 'a').write("Error writing to db\n")
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

    # Prints whichever projects people have, if they have them
    if projects[4]:
        button01 = tk.Button(root,text = projects[4], bg="RoyalBlue1",  command=lambda: saveinfo(ID,projects[4],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button01.grid(pady=2)
        else: button01.grid(pady=10)
    if projects[5]:
        button02 = tk.Button(root,text=projects[5], bg="turquoise4",command=lambda: saveinfo(ID,projects[5],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button02.grid(pady=2)
        else: button02.grid(pady=10)
    if projects[6]:
        button03 = tk.Button(root,text=projects[6], bg="seagreen",  command=lambda: saveinfo(ID,projects[6],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button03.grid(pady=2)
        else: button03.grid(pady=10)
    if projects[7]:
        button04 = tk.Button(root,text=projects[7], bg="RoyalBlue1",command=lambda: saveinfo(ID,projects[7],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button04.grid(pady=2)
        else: button04.grid(pady=10)
    if projects[8]:
        button05 = tk.Button(root,text=projects[8], bg="turquoise4",command=lambda: saveinfo(ID,projects[8],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button05.grid(pady=2)
        else: button05.grid(pady=10)
    if projects[9]:
        button06 = tk.Button(root,text=projects[9], bg="seagreen",  command=lambda: saveinfo(ID,projects[9],name),  width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button06.grid(pady=2)
        else: button06.grid(pady=10)
    if projects[10]:
        button07 = tk.Button(root,text=projects[10], bg="RoyalBlue1",command=lambda: saveinfo(ID,projects[10],name), width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button07.grid(pady=2)
        else: button07.grid(pady=10)
    if projects[11]:
        button08 = tk.Button(root,text=projects[11], bg="turquoise4",command=lambda: saveinfo(ID,projects[11],name), width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button08.grid(pady=2)
        else: button09.grid(pady=10)
    if projects[12]:
        button09 = tk.Button(root,text=projects[12], bg="seagreen", command=lambda: saveinfo(ID,projects[12],name), width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button09.grid(pady=2)
        else: button09.grid(pady=10)
    if projects[13]:
        button10 = tk.Button(root,text=projects[13], bg="turquoise1",command=lambda: saveinfo(ID,projects[13],name), width = '20', height=1, font = ("Helvetica", 24))
        if projects[10]: button10.grid(pady=2)
        else: button10.gird(pady=10)

    button11 = tk.Button(root,text='Clock Off', bg="red", command=lambda: saveinfo(ID,"Clock Off",name), width = '20',height=1, font = ("Helvetica", 24))
    if projects[10]: button11.grid(pady=2)
    else: button11.grid(pady=10)

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
