# Test the connection between Python and MySQL

from getpass import getpass
import pymysql

password = getpass("Enter your MySQL password: ")

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password=password,
        database="hospital_operations"
    )

    print("\nSUCCESS: Python connected to MySQL!")

    connection.close()

except pymysql.MySQLError as error:
    print("\nCONNECTION FAILED")
    print("Error:", error)