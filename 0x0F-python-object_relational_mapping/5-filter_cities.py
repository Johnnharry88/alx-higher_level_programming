#!/usr/bin/python3
# Displays all cities of a given state from state table
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT * FROM 'cities' as 'c' \
                INNER JOIN 'states' as 's' \
                   ON 'c'.state_id' = 's'.id \
                ORDER BY 'c'. 'id'")
    print(", ".join([x[2] for x in a.fetchall() if x[4] == sys.argv[4]]))
