#!/usr/bin/python3
""" a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access the database connection
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    database_connection = MySQLdb.connect(
            host="localhost",
            user=username,
            port=3306,
            passwd=password,
            db=database
            )

    cursor_obj = database_connection.cursor()
    """Create the cursor object"""

    sql = ("SELECT cities.name FROM cities INNER JOIN states \
            ON cities.state_id = states.id WHERE states.name = %s")
    cursor_obj.execute(sql, (state_name,))
    selected_rows = cursor_obj.fetchall()
    for row in selected_rows:
        print(row)

    cursor_obj.close()
    database_connection.close()
