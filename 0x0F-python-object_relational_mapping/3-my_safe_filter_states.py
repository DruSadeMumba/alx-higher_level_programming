#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
and is safe from MySQL injections
"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur = conn.cursor()
    cur.execute(query, (name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
