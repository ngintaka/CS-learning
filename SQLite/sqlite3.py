# -*- coding: utf-8 -*-
'''Sample SQLite3 python scripts'''

# http://zetcode.com/db/sqlitepythontutorial/

import sqlite3 as lite #import sqlite3 module
import sys

con = lite.connect('test.db') #open or create db

with con:
    cur = con.cursor() #get cursor for db  
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)") #create new table
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)") #add data to table row by row
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")

'''OR use the executemany() method to create a table from an iterable'''

#using a tuple of tuples for the data
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars) #method takes a paramaterized SQL statement and data
    
    lastID = cur.lastrowid
    print "Last row ID is %s" % lastID
    
#auto-incremented primary key     
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);") # "integer primary key" is auto incremented
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');") # changed syntax for autoincremented insertions;
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');") # explicitly state col names but not autoincremented
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    
    
 '''Fetching data from db'''


with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars") #execute SQL statement

    rows = cur.fetchall() # then fetch resulting data

    for row in rows:
        print row
        
''' or print row by row

while True:
    row = cur.fetchone()
    if row = None:
        break
    print row[0], row[1], row[2]                                           
'''                                                                           
        
''' dictionary cursor to access by col name
with con:    
    con.row_factory = lite.Row
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars") #execute SQL statement

    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" %(row["Id"], row["Name"], row["Price"])
'''     

'''UPDATE a field      
uId = 1
uPrice = 62300 

con = lite.connect('test.db')

with con:

    cur = con.cursor()    

    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))        
    con.commit()
    
    print "Number of rows updated: %d" % cur.rowcount
'''      
        