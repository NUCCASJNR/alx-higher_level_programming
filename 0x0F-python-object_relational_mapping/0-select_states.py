#!/usr/bin/python3
"""
This a script that lists all states from the
database hbtn_0e_0_usa
:"""
import MySQLdb
import sys
"""
Import the MySQLdb and sys module
"""

if __name__ == "__main__":
    """
    Access the database
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
    cursor_obj.execute("SELECT * FROM states")
    selected_rows = cursor_obj.fetchall()
    for row in selected_rows:
        print(row)
    cursor_obj.close()
    db.close()
