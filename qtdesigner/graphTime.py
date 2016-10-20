import sys
import MySQLdb


#scope is how many weeks to collect from (1 = up to 1 week from today)
#group is the string of the group (e.g. "PE")
def graph(scope,group):

    try:
        #connect SQL database
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

        #set cursor
        cursor = db.cursor()

        #finds number of users
        cursor.execute("SELECT COUNT(username) FROM users")
        result = str(cursor.fetchall()) #fetches as a string
        numOfUsers = int(result[2:-5]) #cuts it down to only a number
    
        print numOfUsers
        db.close()
            
    except:
        db.close()
        print("Failed to counter users from db")
        #tkMessageBox.showwarning("header", "Failed to write to database. \n\nContact Teal")


    
    #print durr
    #print group

if __name__ == '__main__':
    graph(1,"PE")
    
