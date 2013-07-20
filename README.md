pypyodbc
========

A pure Python Cross Platform ODBC interface module

**This is a modified version which is compatible with Informix Client SDK 3.50/3.70 for Mac OS X.**

Features
--------

  * One pure Python script, runs on CPython / IronPython / PyPy , Python 3.3 / 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit
  * Almost totally same usage as pyodbc (can be seen as a re-implementation of pyodbc in pure Python via ctypes)
  * Simple - the whole module is implemented in a single python script with less than 3000 lines
  * Built-in Access MDB file creation and compression functions on Windows 

Simply try pypyodbc:

    import pypyodbc 
    pypyodbc.win_create_mdb('D:\\database.mdb')
    connection_string = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=D:\\database.mdb'
    connection = pypyodbc.connect(connection_string)
    SQL = 'CREATE TABLE saleout (id COUNTER PRIMARY KEY,product_name VARCHAR(25));'
    connection.cursor().execute(SQL)
    ...

BBS
---

http://tech.groups.yahoo.com/group/pypyodbc/messages


Install
-------

Install this modified version from GitHub:

    pip install git+https://github.com/rockallite/pypyodbc-informixcsdk.git#egg=pypyodbc-informixcsdk

Uninstall

    pip uninstall pypyodbc-informixcsdk

If you want to install the ORIGINAL version:

    pip install pypyodbc

Or get the latest pypyodbc.py script from GitHub (Main Development site) <https://github.com/jiangwen365/pypyodbc>
