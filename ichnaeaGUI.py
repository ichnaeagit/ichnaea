#!/user/bin/env python

#export PATH="/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/mysql/bin:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/platform-tools:~/usr/lib/jvm/jdk-6/bin


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
##        button01.destroy()
##        button02.destroy()
##        button03.destroy()
##        button04.destroy()
##        button05.destroy()
##        button06.destroy()
##        button07.destroy()
##        button08.destroy()
##        button09.destroy()
##        button10.destroy()
##        nameLabel.destroy()
##        helpText.destroy()
        
               


    def buttonPressed():
            print 'Please scan your card'
            project = int()
            project = 0
          
            
            
            # Run program to scan card info to file
            name, ID = cardRead.readAndSave()
            
            userName = tk.StringVar()
            tempName = 'Hello '
            tempName +=name        
            userName.set(tempName)
            
            nameLabel =tk.Label(root, textvariable=userName, font=("Helvetica",12))
            nameLabel.pack(pady=1)
            helpText = tk.Label(root, text='Please pick a project', fg="blue")
            helpText.pack(pady=3)

            #LETS ME DELETE LATER
            #global button01, button02, button03, button04, button05, button06, button07, button08, button09, button10, nameLabel, helpText
            button01 = tk.Button(root,text='CAPA Projects', bg="orange", command=lambda: saveinfo(ID,1), width = '50', height=3)
            button01.pack(pady=2)
            button02 = tk.Button(root,text='Packaging Support', bg="blue", fg='white',command=lambda:saveinfo(ID,2), width = '50',height=3)
            button02.pack(pady=2)
            button03 = tk.Button(root,text='Operations Support', bg="cyan", command=lambda: saveinfo(ID,3), width = '50',height=3)
            button03.pack(pady=2)
            button04 = tk.Button(root,text='MCDR/WCR', bg="Yellow", command=lambda: saveinfo(ID,4), width = '50',height=3)
            button04.pack(pady=2)
            button05 = tk.Button(root,text='Cost Savings Projects', bg="red", command=lambda: saveinfo(ID,5), width = '50',height=3)
            button05.pack(pady=2)
            button06 = tk.Button(root,text='Product Transfer Support', bg="orange", command=lambda: saveinfo(ID,6), width = '50',height=3)
            button06.pack(pady=2)
            button07 = tk.Button(root,text='Training', bg="blue", command=lambda: saveinfo(ID,7), fg='white', width = '50',height=3)
            button07.pack(pady=2)
            button08 = tk.Button(root,text='Research Projects', bg="cyan", command=lambda: saveinfo(ID,8), width = '50',height=3)
            button08.pack(pady=2)
            button09 = tk.Button(root,text='Meetings', bg="yellow", command=lambda: saveinfo(ID,9), width = '50',height=3)
            button09.pack(pady=2)
            button10 = tk.Button(root,text='Clock Off', bg="red", command=lambda: saveinfo(ID,10), width = '50',height=3)
            button10.pack(pady=5)
        

    class MainApplication(tk.Frame):
        def __init__(self,parent, *args, **kwargs):
            tk.Frame.__init__(self,parent, *args, **kwargs)
            self.parent = parent
            root.geometry('600x900+350+50')
            #main GUI here

            quitButton = tk.Button(root, text='Quit program', bg="red", fg ="black",height=1,font=("Helvetica",9), command = quitProgram)
            quitButton.pack(pady=1)

            welcomeText = tk.Label(root, text="Ichnaea time tracking Beta\n V0.0.1", font=("papyrus",12), fg="blue", width=20)
            welcomeText.pack(pady=5)

            helpText = tk.StringVar()
            helpText.set('Swipe until project picker appears')
            
            #scanButton = tk.Button(root,text='Click here to scan', bg="red", fg="white", height = 3, font=("Helvetica",16), command = buttonPressed)
            #scanButton.pack(padx=5, pady=3)

            scanCard = tk.Label(root, text="Please Scan Card", font=("papyrus",24), fg="red", width=20)
            scanCard.pack(pady=10)
            
            feedbackLabel = tk.Label(root, textvariable=helpText, fg="blue")
            feedbackLabel.pack(pady=5)

            
            root.after(500, buttonPressed)


    if __name__ == "__main__":
        root = tk.Tk()
        MainApplication(root).pack(side="top",fill="both",expand=True)
        root.mainloop()


   



