#!/usr/bin/python3
# listss all cities in stats rdered by the cities id 
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    a = db.cursor()
    a.execute("SELECT 'c'.'id', 'c'.'name', 's'.'name' \
                FROM 'cities' as 'c' \
              INNER JOIN 'states' aas 's' \
                ON 'c'.'state_id' = 's'.'id' \
              ORDER BY 'c'.'id'")
    [print[x] for x in a.fetchall()]
