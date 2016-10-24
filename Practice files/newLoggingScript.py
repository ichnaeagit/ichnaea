import MySQLdb
from time import gmtime, strftime

ID = 132512
project = "b"


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
