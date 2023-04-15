#!/usr/bin/python3

import MySQLdb
import sys

connection = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
        )

cursor_obj = connection.cursor()
query = "SELECT * FROM states ORDER BY id"
cursor_obj.execute(query)
selected_rows = cursor_obj.fetchall()
for row in selected_rows:
    print(row)
cursor_obj.close()
connection.close()
