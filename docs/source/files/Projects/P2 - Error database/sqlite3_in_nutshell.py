import sqlite3 ###--> in the python standard library

#https://www.pythoncentral.io/introduction-to-sqlite-in-python


###to create a database:
db = sqlite3.connect('paranal_error.db')  ##<---this creates or loads the database (if already exist)


####create a new table: 
cursor = db.cursor() ###<---needed to make any operation with the database, it is an object
cursor.execute('''CREATE TABLE IF NOT EXISTS error(instrument TEXT, occurence TEXT, error_name TEXT, last TEXT, troubleshoot TEXT)''')
####this creates a table, only if one with the same name does not exist already
db.commit()   ###save the change

#####add an entry
cursor.execute('INSERT INTO error(instrument, occurence, error_name, last, troubleshoot) VALUES(?,?,?,?,?)', ('xshoot', 1, 'Error1', '2018-01-15 23:35:49', 'fix' ))
cursor.execute('INSERT INTO error(instrument, occurence, error_name, last, troubleshoot) VALUES(?,?,?,?,?)', ('xshoot', 1, 'Error2', '2018-01-15 23:35:49', 'fix' ))
cursor.execute('INSERT INTO error(instrument, occurence, error_name, last, troubleshoot) VALUES(?,?,?,?,?)', ('flames', 1, 'ErrorA', '2018-01-15 23:30:49', 'fix' ))
cursor.execute('INSERT INTO error(instrument, occurence, error_name, last, troubleshoot) VALUES(?,?,?,?,?)', ('UVES', 1, 'ErrorA', '2018-01-15 23:30:49', 'fix' ))

db.commit()


###query to the database
a = db.execute("SELECT * FROM error WHERE instrument = ? AND error_name = ?", ('xshoot', 'Error2'))
for i in a:
    print(i)

####update an entry
cursor.execute("UPDATE error SET occurence = 5 WHERE instrument = ? AND error_name = ?", ('xshoot', 'Error2'))
db.commit()

###query to the database
a = db.execute("SELECT * FROM error WHERE instrument = ? AND error_name = ?", ('xshoot', 'Error2'))
for i in a:
    print(i)

###remove a table
db.execute('DROP TABLE error')
###close the database
db.close()
