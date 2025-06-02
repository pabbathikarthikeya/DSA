import mysql.connector

# Corrected the hostname from 'loaclhost' to 'localhost'
mydb = mysql.connector.connect(
    user='root',
    passwd='root',
    host='localhost'
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)
