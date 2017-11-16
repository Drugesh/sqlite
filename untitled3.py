#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('testDB.db')
print ("Opened database successfully");

conn.execute("INSERT INTO Inventory (ID,MACHINENAME,IP,RAM,DIMMSTATS,HDDBAY,SSD,SSDTYPE,CONSOLEIP,CONSOLE,NOOFHDD,HDDCAPACITY,STORAGE,OWNER,PROJECT,LEASETIME,TIMETOEXPIRE) \
      VALUES (2, 'DJtest2', '10.10.10.94', '32GB', 'NA','10.10.10.92','50GB','Flash','10.10.10.78','10.10.10.74','15', '500GB','1TB','Drugesh','ITR','1 months','4 days')");


conn.commit()
print ("Records created successfully");
conn.close()
