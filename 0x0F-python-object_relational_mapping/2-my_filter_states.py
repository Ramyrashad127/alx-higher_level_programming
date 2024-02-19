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
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'\
            ORDER BY id ASC".format(argv[4]))
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    con.close()
