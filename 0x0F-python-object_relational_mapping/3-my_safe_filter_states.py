#!/usr/bin/python3

import MySQLdb
import sys
"""
Import the necessary modules
"""

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            passwd=password,
            db=database
            )
    cursor_obj = db.cursor()
    """
    Creates the cursor object
    """
    sql = ("SELECT id, name FROM states WHERE name = ? ORDER BY id  ASC")
    prepared = cursor.prepare(sql)
    args = ('state_name',)
    cursor_obj.execute(sql, prepared, args)
    selected_row = cursor_obj.fetchall()
    for i in selected_row:
        print(i)
    cursor_obj.close()
    db.close()
