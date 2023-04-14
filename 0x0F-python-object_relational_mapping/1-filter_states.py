#!/usr/bin/python3
"""
 a script that lists all states with a name startin
g with N (upper N) from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys
"""
Import the MySQLdb and sys modules
"""

if __name__ == "__main__":
    """
    create the connection
    """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            port=3306,
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor_obj = db.cursor()
    """
    Creates the cursor object
    """
    cursor_obj.execute(
            "SELECT *  FROM states WHERE name LIKE  BINARY'N%' \
                    ORDER BY states.id ASC")
    selected_row = cursor_obj.fetchall()
    for i in selected_row:
        print(i)
    cursor_obj.close()
    db.close()
