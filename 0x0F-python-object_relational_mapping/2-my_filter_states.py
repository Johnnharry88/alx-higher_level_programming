#!/usr/bin/python3
# Displays all states with vlaue matchin the supplied argument
import sys
import MySQLdb

if __name == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * \
                FROM 'states' \
               WHERE BINARY 'name' = '{}'".format(sys,argv[4]))
    [print(x) for x in a.fetchall()]
