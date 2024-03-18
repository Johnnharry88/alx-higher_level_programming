#!/usr/bin/python3
"""Displays all values in the states whose name matches those supplied as an argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM states")
    [print(x) for x in a.fetchall() if x[1] == sys.argv[4]]
