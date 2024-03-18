#!/usr/bin/python3
"""Scripts that list all states having a in it"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    [print(a) for a in c.fetchall() if a[1][0] == 'N']
