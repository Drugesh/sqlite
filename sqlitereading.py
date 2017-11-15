import sqlite3
import sys

conn = sqlite3.connect('testDB.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT id, name, address, salary from company")
flag=0;
for row in cursor:
    name=sys.argv[1]
    if name==row[1]:
        print( "ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")
        flag=1;


if flag==0:
         print("Invalid Name")
conn.close()
