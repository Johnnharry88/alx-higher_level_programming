#!/usr/bin/python3
# lists all state from the tatabase htn_0e_0_usa
import sys
import MySQLdb
if __name__ == '__main__':
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],db=sys.argv[3])
    x = db.cursor()
    x.execute("SELECT * FROM 'states'")
    [print(state) for state in x.fetchall()]
