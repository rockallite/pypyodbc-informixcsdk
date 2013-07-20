pypyodbc
========

A pure Python Cross Platform ODBC interface module

**This is a modified version which is compatible with Informix Client SDK 3.50 / 3.70 for Mac OS X. For instructions on how to connect to a Informix database from a Mac in Python, see the wiki.**

Features
--------

  * One pure Python script, runs on CPython / IronPython / PyPy , Python 3.3 / 2.4 / 2.5 / 2.6 / 2.7 , Win / Linux , 32 / 64 bit
  * Almost totally same usage as pyodbc (can be seen as a re-implementation of pyodbc in pure Python via ctypes)
  * Simple - the whole module is implemented in a single python script with less than 3000 lines
  * Built-in Access MDB file creation and compression functions on Windows
  * Informix Client SDK for Mac OS X support

Simply try pypyodbc:

    import pypyodbc 
    conn = pypyodbc.connect(driver='iclit09b.dylib', server='your_server', db='your_db',
                            uid='your_username', pwd='your_password')
    cursor = conn.cursor()
    cursor.execute('CREATE TEMP TABLE ttbl1 (num DECIMAL(14, 2))')
    cursor.execute('INSERT INTO ttbl1 VALUES (NULL)')
    cursor.execute('SELECT num FROM ttbl1')
    cursor.fetchone()

BBS
---

http://tech.groups.yahoo.com/group/pypyodbc/messages


Install
-------

Install this modified version from GitHub:

    pip install git+https://github.com/rockallite/pypyodbc-informixcsdk.git

Uninstall

    pip uninstall pypyodbc-informixcsdk

If you want to install the ORIGINAL version:

    pip install pypyodbc

Or get the latest pypyodbc.py script from GitHub (Main Development site) <https://github.com/jiangwen365/pypyodbc>
