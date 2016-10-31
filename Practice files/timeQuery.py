import MySQLdb
from time import gmtime, strftime
import urllib2

ID = 323877
project = "b"


#save username, clocknum, project, timestamp, and durration to db
try:
    db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
    cursor = db.cursor()

    # get the last log for user, and find durration difference
    getTimeLogs = "SELECT logtime, nextProject FROM logs WHERE clockNum = '%d'" % (ID)
    cursor.execute(getTimeLogs)
    logtimes = cursor.fetchall()

    # extract the last log of the
    lastLog = logtimes[-1]

    # Extract the last project they logged into
    loggedProject = lastLog[-1]
    
    lastLog = str(lastLog)
    lastLog = lastLog.split()
    lastLog = [s.strip('(datetime.datetime(') for s in lastLog]
    lastLog = [s.strip('),)') for s in lastLog]

    print lastLog

    db.close()

except:
    print "error!"
    db.close()

pageURL = urllib2.urlopen("http://just-the-time.appspot.com")
timeDate = pageURL.read()

timeDate = timeDate.replace('-',' ')
timeDate = timeDate.replace(':',' ')
timeDate = timeDate.split()
print timeDate

##try:
##    db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
##    cursor = db.cursor()
##
##    cursor.exectue("SELECT CURRENT_TIMESTAMP")
##    print "here"
##    currentTime = cursor.fetchall()
##
##    print currentTime
##except:
##    print "error in current time"
##    db.close()

##    # get current time
##    time = strftime("%Y %m %d %H %M %S", gmtime())
##    time = time.split()
##
##    #print "current time is:"
##    #print time
##    # store time differences
##    secDiff = float(time[5]) - float(lastLog[5])
##    minDiff = float(time[4]) - float(lastLog[4])
##    hourDiff = float(time[3]) - float(lastLog[3])
##    dayDiff = float(time[2]) - float(lastLog[2])
##    monthDiff = float(time[1]) - float(lastLog[1])
##    yearDiff = float(time[0]) - float(lastLog[0])
