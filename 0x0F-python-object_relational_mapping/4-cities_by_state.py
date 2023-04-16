#!/usr/bin/python3
"""This script displays all the values of a given
    table where name matches the argument"""
import MySQLdb
import sys


def main():
    """The main function to be executed"""
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM states s INNER JOIN "
                   "cities c ON s.id = c.state_id ORDER by c.id ASC;")
    states = cursor.fetchall()
    for _ in states:
        print(_)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
