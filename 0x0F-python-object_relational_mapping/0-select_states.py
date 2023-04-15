#!/usr/bin/python3
"""This scripts list all the states in a given database"""
import MySQLdb
import sys


def main():
    """The main function; not to be executed if the script is imported"""
    db = MySQLdb.connect(host='localhost:3306', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY states.id ASC;")
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
