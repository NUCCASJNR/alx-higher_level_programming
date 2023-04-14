#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
"""
import the MySQLdb and sys module
"""

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            port=3306,
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cursor_obj = db_connection.cursor()
    """
    Create the cursor object
    """
    sql = ("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states on cities.state_id\
            = states.id ORDER BY cities.id ASC")
    cursor_obj.execute(sql)
    selected_rows = cursor_obj.fetchall()
    for row in selected_rows:
        print(row)

    cursor_obj.close()
    db_connection.close()
