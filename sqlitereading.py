import sqlite3
import sys

conn = sqlite3.connect('testDB.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT * from inventory")
flag=0;
for row in cursor:
    arg=sys.argv[1]
    if arg in row:
        print( "ID = ", row[0])
        print ("MACHINENAME = ", row[1])
        print ("IP = ", row[2])
        print ("RAM = ", row[3], "\n")
	print ("DIMMSTATS = ", row[4])
	print ("HDDBAY = ", row[5])
	print ("SSD = ", row[6])
	print ("SSDTYPE = ", row[7])
	print ("CONSOLEIP = ", row[8])
	print ("CONSOLE = ", row[9])
	print ("NOOFHDD = ", row[10])
	print ("HDDCAPACITY = ", row[11])
	print ("STORAGE = ", row[12])
	print ("OWNER = ", row[13])
	print ("PROJECT = ", row[14])
	print ("LEASETIME = ", row[15])
	print ("TIMETOEXPIRE = ", row[16])
        flag=1;

if flag==0:
         print("Invalid Name")
conn.close()
