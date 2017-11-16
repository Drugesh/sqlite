#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:09:59 2017

@author: admin
"""

import sqlite3

conn = sqlite3.connect('testDB.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE inventory
         (ID INT PRIMARY KEY     NOT NULL,
         MACHINENAME           TEXT    NOT NULL,
         IP            TEXT     NOT NULL,
         RAM        CHAR(50),
         DIMMSTATS         REAL,
	HDDBAY        CHAR(50),
SSD           TEXT    NOT NULL,
SSDTYPE           TEXT    NOT NULL,
CONSOLEIP           TEXT    NOT NULL,
CONSOLE           TEXT    NOT NULL,
NOOFHDD           TEXT    NOT NULL,
HDDCAPACITY           TEXT    NOT NULL,
STORAGE           TEXT    NOT NULL,
OWNER           TEXT    NOT NULL,
PROJECT           TEXT    NOT NULL,
LEASETIME           TEXT    NOT NULL,
TIMETOEXPIRE           TEXT    NOT NULL);''')

print( "Table created successfully");

conn.close()
