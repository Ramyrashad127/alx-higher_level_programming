#!/usr/bin/python3
"""import for sys and mysqldb"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    con.close()
