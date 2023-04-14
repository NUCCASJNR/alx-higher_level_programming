#!/usr/bin/python3

"""
script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
 """

import MySQLdb
import sys
"""
Import the MySQLdb and sys modules
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
    sql = ("SELECT id, name FROM states WHERE name = %s ORDER BY id  ASC")
    cursor_obj.execute(sql, (state_name,))
    selected_row = cursor_obj.fetchall()
    for i in selected_row:
        print(i)
    cursor_obj.close()
    db.close()
