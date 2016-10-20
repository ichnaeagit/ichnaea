import sys
import MySQLdb
import tkMessageBox




def countUsers():
    try:
        #connect SQL database
        db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

        #set cursor
        cursor = db.cursor()

        #finds number of users
        cursor.execute("SELECT COUNT(username) FROM users")
        result = str(cursor.fetchall()) #fetches as a string
        numOfUsers = int(result[2:-5]) #cuts it down to only a number
    
        return numOfUsers
        db.close()
            
    except:
        db.close()
        print("Failed to count users from db")
        sys.exit()

# ---- main ----
#scope is how many weeks to collect from (1 = up to 1 week from today)
#groups is the string of the group (e.g. "PE")

def graph(scope,groups):
    numOfUsers = countUsers()
    print "There are %s users" % (numOfUsers)

    #Saves RFID numbers for each person in the selected groups
    i=0
    userSearchRFIDs = []

    for group in groups:
        i=i+1
        
        try:
            db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
            cursor = db.cursor()

            query = "SELECT rfidnum FROM users WHERE groupname = '%s'" % (group)
            cursor.execute(query)
            result = str(cursor.fetchall()) #fetches data
            result = result[1:-1]   #cuts off end shit
            result = result.split() #cuts into bit
            result = [s.strip('L,)') for s in result]   #strips out shit
            result = [s.strip('(') for s in result]     #strips out other shit

            userSearchRFIDs.append(group)
            userSearchRFIDs.append(result)
            #userSearchRFIDs[i].append(result)
            #print result

            db.close()
        except:
            print "error!"
            db.close()
            sys.exit()
            

    
    print userSearchRFIDs
        
    
    #print durr
    #print group

if __name__ == '__main__':
    graph(1,["PE","QE"])
    
