import sys
import MySQLdb
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def getGraphInfo(allUsers, scope):
    graphLogs = []

    # for every user in the list of all available users (broken down by group)
    for group in allUsers:

        # since it is broken up into groups of PE, QE etc, go through each one of 
        for user in group:

            user = int(user) #makes sure user is just a number
            
            try:
                db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
                cursor = db.cursor()

                # creates queries, based on clock numbers and time scope in weeks. If scope = 0, take all time data
                if scope != 0:
                    getDurr = "SELECT logdurr FROM logs WHERE clockNum = '%d' AND logtime > CURRENT_DATE - INTERVAL '%d' WEEK" % (user, scope)
                else:
                    getDurr = "SELECT logdurr FROM logs WHERE clockNum = '%d'" % (user)

                getName = "SELECT username FROM users WHERE clockNum = '%d'" % (user)

                # Get the username of the person, for easy graphing
                cursor.execute(getName)
                name = str(cursor.fetchall())
                name = name[3:-5]
                graphLogs.append(name) # saves username

                # get their summed durration
                cursor.execute(getDurr)
                durr = str(cursor.fetchall())
                durr = durr[2:-5]   #cuts off end shit
                durr = durr.split() #cuts into bit
                durr = [s.strip('L,)') for s in durr]   #strips out shit
                durr = [s.strip('(') for s in durr]     #strips out other shit

                # takes array of durration, sums
                time = float(0)
                for t in durr:

                    # For times when the time is null, etc
                    try:
                        time = time + float(t)
                    except:
                        time = time

                graphLogs.append(time) #saves clocked time in (hours?)

                db.close()
            except:
                db.close()
                print "error!"
    
    return graphLogs
    

def getUsers(groups):

    #Saves RFID numbers for each person in the selected groups
    
    users = []

    #print groups
    
    for group in groups:

        try:
            db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
            cursor = db.cursor()

            query = "SELECT clocknum FROM users WHERE groupname = '%s' " % (group)
            cursor.execute(query)
            result = str(cursor.fetchall()) #fetches data

            #print group
            
            result = result[1:-1]   #cuts off end shit
            result = result.split() #cuts into bit
            result = [s.strip('L,)') for s in result]   #strips out shit
            result = [s.strip('(') for s in result]     #strips out other shit

            #users.append(group)
            users.append(result)
            #users[i].append(result)
            #print result

            db.close()
        except:
            print "error!"
            db.close()
            sys.exit()
    # returns 2d array of clock numbers which are within criteria, segregated by group 
    return users

def graphData(graphInfo):

    barNames = []
    durrations = []
    for name in graphInfo:
        if isinstance(name, basestring): barNames.append(str(name))
        else: durrations.append(float(name))

    y_pos = np.arange(len(barNames))
    plt.bar(y_pos, durrations, align = 'center', alpha = 0.5)
    plt.xticks(y_pos, barNames)
    plt.title("Time plot by user")
    plt.ylabel('Minutes')
    plt.show()
    

#
#
#
# ---- main ----
#scope is how many weeks to collect from (1 = up to 1 week from today)
#groups is the string of the group (e.g. "PE")

def graph(scope,groups):

    allUsers = getUsers(groups)

    graphInfo = getGraphInfo(allUsers, scope)

    graphData(graphInfo)

    return graphInfo

if __name__ == '__main__':
    graph(0,["PE","QE"])
    #graph(1,["PE"])
    
