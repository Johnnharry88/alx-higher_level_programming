#!/usr/bin/python3
# list all states with name starting with N form database
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    x = db.cursor()
    x.execute("SELCET * FROM 'states' ORDER BY 'id'")
    [print(a) for a in c.fetchall() if a[1][0] = "N"] 
