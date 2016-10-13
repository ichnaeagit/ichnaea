import Tkinter as tk
import tkMessageBox
import cardReadModule as cardRead
import sys
import MySQLdb
import time



continuousRun = True


while continuousRun:

    def quitProgram():
        continuousRun = False
        root.destroy()
        sys.exit()

    def saveinfo(ID, project):

        try:
            #write to SQL database
            db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

            try:
                cursor = db.cursor()
                args = (ID, project)
                # Catches errors
                query = "INSERT INTO logs(clockNum, logproject)" \
                    "VALUES (%s,%s)"

                cursor.execute(query, args)

                db.commit()
                print("Committed to DB")
                db.close()
            
            except:
                db.rollback()
                db.close()
                print("Failled to write to DB")
                tkMessageBox.showwarning("header", "Failed to write to database. \n\nContact Teal")

        except:
            print("Failed connect to db")
            tkMessageBox.showwarning("header", "Failed to connect to database.\n\nCheck ethernet cord, or contact Teal")        
        
        root.destroy()

    def buttonPressed():
        print 'Please scan your card'
        project = int()
        project = 0

        # Run program to scan card info to file
        name, ID = cardRead.readAndSave()

        # Only runs rest of code if there is a valid ID optained
        if ID:
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
        

    class MainApplication(tk.Frame):
        def __init__(self,parent, *args, **kwargs):
            tk.Frame.__init__(self,parent, *args, **kwargs)
            self.parent = parent
            root.geometry('600x900+350+50')
            #main GUI here


            quitButton = tk.Button(root, text='Quit program', bg="red", fg ="black",height=1,width=85,font=("Helvetica",9), command = quitProgram)
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


   



