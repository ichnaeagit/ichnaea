import MySQLdb
from time import gmtime, strftime

ID = 132512


#save username, clocknum, project, timestamp, and durration to db
try:
    db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")
    cursor = db.cursor()

    query = "SELECT logtime FROM logs WHERE clockNum = '%d'" % (ID)
    cursor.execute(query)
    logtimes = cursor.fetchall()
    lastLog = logtimes[-1]
    lastLog = str(lastLog)
    lastLog = lastLog.split()
    lastLog = [s.strip('(datetime.datetime(') for s in lastLog]
    lastLog = [s.strip('),)') for s in lastLog]

    print lastLog

    time = strftime("%Y %m %d %H %M %S")
    time = time.split()

    print time
    
    secDiff = float(time[5]) - float(lastLog[5])
    minDiff = float(time[4]) - float(lastLog[4])
    hourDiff = float(time[3]) - float(lastLog[3])
    dayDiff = float(time[2]) - float(lastLog[2])
    monthDiff = float(time[1]) - float(lastLog[1])
    yearDiff = float(time[0]) - float(lastLog[0])

    timeDiffMin = (hourDiff * 60) + minDiff + (secDiff / 60)

    if timeDiffMin > (360):
        timeDiffMin = 360

    if dayDiff or monthDiff or yearDiff:
       timeDiffMin = 0

    print timeDiffMin
    
    db.close()
except:
    print "error!"
    db.close()
