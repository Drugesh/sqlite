#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:09:59 2017

@author: admin
"""

import sqlite3

conn = sqlite3.connect('testDB.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print( "Table created successfully");

conn.close()