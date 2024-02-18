#!/usr/bin/python3
"""import for sys and mysqldb"""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states")
    data = cur.fetchall()
    for i in data:
        print(i)
    cur.close()
    con.close()
