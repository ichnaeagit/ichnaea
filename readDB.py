import MySQLdb

# connected
db = MySQLdb.connect("MUDDJ2-D1","RP","12345678","ichnaeadb")

cursor = db.cursor()


idnum = 13644974
# find where id = id stored, and returns id name
sql = "SELECT username FROM users WHERE rfidnum = '%d'" % (idnum)

try:
    # does the thing
    cursor.execute(sql)
    # fetch the username as a string
    results = str(cursor.fetchone())
    # cuts the ends by 2 and 3 respectivily to take off random trash
    results = results[2:-3]
    if results:
        print results
    else:
        print "No user found"
except:
    print "Error"
# close db
db.close()
