from qgb import U,T,Clipboard
import os,sys;basedir=os.path.dirname(__file__)
# basedir=r'''D:\test'''
import sqlite3
fdb=basedir+'\\v.db'
print fdb
# U.x()
conn = sqlite3.connect(fdb)
def execsql(sql):
	global conn
	if sql is not None and sql != '':
		cu =conn.cursor()
		print('{}'.format(sql))
		cu.execute(sql)
		conn.commit()
	else:
		print('the [{}] is empty or equal None!'.format(sql))
execsql('''create table v(
uid INT PRIMARY KEY,
vid INT  NOT NULL,
time varchar(20))''')
# execsql('insert into ta(t) values(1)')