import Tkinter as tk
import tkMessageBox
import cardReadModule as cardRead
import sys
import MySQLdb
import time
import readID
from time import gmtime, strftime



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

        # get current time
        time = strftime("%Y %m %d %H %M %S", gmtime())
        time = time.split()

        #print "current time is:"
        #print time
        # store time differences
        secDiff = float(time[5]) - float(lastLog[5])
        minDiff = float(time[4]) - float(lastLog[4])
        hourDiff = float(time[3]) - float(lastLog[3])
        dayDiff = float(time[2]) - float(lastLog[2])
        monthDiff = float(time[1]) - float(lastLog[1])
        yearDiff = float(time[0]) - float(lastLog[0])
       
        # set minute differences
        timeDiffMin = (hourDiff * 60) + minDiff + (secDiff / 60)
        # adds offset from some error in time differences
        timeDiffMin = timeDiffMin + 4.0

        # if someone clocks on for over 360min, then count only as 360 min
        if timeDiffMin > (360):
            timeDiffMin = 360

        # if they don't log off, give them them 360min
        if dayDiff or monthDiff or yearDiff:
           timeDiffMin = 360

        # make sure to not count time off
        if loggedProject == "Clock Off":
            timeDiffMin = 0
        
        db.close()
    except:
        print "error!"
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
        print "commited log durr"

    except:

        print "error writing to db"
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
        userName = tk.StringVar()
        tempName = 'Hello '
        tempName +=name        
        userName.set(tempName)
        userName='Please try again'

        # Prints names
        nameLabel =tk.Label(root, textvariable=userName, font=("Helvetica",12))
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
        button01 = tk.Button(root,text = projects[4], bg="orange", command=lambda: saveinfo(ID,projects[4]), width = '50', height=3)
        button01.grid()
        if projects[5]:
            button02 = tk.Button(root,text=projects[5], bg="blue", fg='white',command=lambda:saveinfo(ID,projects[5]), width = '50',height=3)
            button02.grid()
        if projects[6]:
            button03 = tk.Button(root,text=projects[6], bg="cyan", command=lambda: saveinfo(ID,projects[6]), width = '50',height=3)
            button03.grid()
        if projects[7]:
            button04 = tk.Button(root,text=projects[7], bg="Yellow", command=lambda: saveinfo(ID,projects[7]), width = '50',height=3)
            button04.grid()
        if projects[8]:
            button05 = tk.Button(root,text=projects[8], bg="red", command=lambda: saveinfo(ID,projects[8]), width = '50',height=3)
            button05.grid()
        if projects[9]:
            button06 = tk.Button(root,text=projects[9], bg="orange", command=lambda: saveinfo(ID,projects[9]), width = '50',height=3)
            button06.grid()
        if projects[10]:
            button07 = tk.Button(root,text=projects[10], bg="blue", command=lambda: saveinfo(ID,projects[10]), fg='white', width = '50',height=3)
            button07.grid()
        if projects[11]:
            button08 = tk.Button(root,text=projects[11], bg="cyan", command=lambda: saveinfo(ID,projects[11]), width = '50',height=3)
            button08.grid()
        if projects[12]:
            button09 = tk.Button(root,text=projects[12], bg="yellow", command=lambda: saveinfo(ID,projects[12]), width = '50',height=3)
            button09.grid()
        button10 = tk.Button(root,text='Clock Off', bg="red", command=lambda: saveinfo(ID,"Clock Off"), width = '50',height=3)
        button10.grid()
    else: root.destroy()

while continuousRun:

    class MainApplication(tk.Frame):
        def __init__(self,parent, *args, **kwargs):
            tk.Frame.__init__(self,parent, *args, **kwargs)
            self.parent = parent
            root.geometry('475x750+0+0')
            #main GUI here


            quitButton = tk.Button(root, text='Quit program', bg="red", fg ="black",height=1,width=65,font=("Helvetica",9), command = quitProgram)
            quitButton.grid()

            welcomeText = tk.Label(root, text="Ichnaea time tracking Beta\n V0.0.1", font=("papyrus",12), fg="blue", width=20)
            welcomeText.grid()

            helpText = tk.StringVar()
            helpText.set('Swipe until project picker appears')
            
            #scanButton = tk.Button(root,text='Click here to scan', bg="red", fg="white", height = 3, font=("Helvetica",16), command = buttonPressed)
            #scanButton.pack(padx=5, pady=3)

            scanCard = tk.Label(root, text="Please Scan Card", font=("papyrus",24), fg="red", width=20)
            scanCard.grid(row=3, column=0,columnspan=2,pady=10)
            
            feedbackLabel = tk.Label(root, textvariable=helpText, fg="blue")
            feedbackLabel.grid()
            
            root.after(500, buttonPressed)

    if __name__ == "__main__":
        root = tk.Tk()
        root.title("Ichnaea time tracking")
        #MainApplication(root).pack(side="top",fill="both",expand=True)
        display = MainApplication(root)
        root.mainloop()


   



