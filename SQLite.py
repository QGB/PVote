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
	try:
		cu =conn.cursor()
		cu.execute(sql)
		conn.commit()
		if U.debug: print('{}'.format(sql))
		return cu.fetchall()
	except Exception as e:
		print(e)
exe=sql=execsql

import time
def vote(vid):#sql injection
	vid=int(vid)
	if(vid<0 or vid>9):raise Exception('vid %s out of range '%(vid))
	exe('insert into v(vid,time) values(%s,%s)'%(vid,time.time()))

def calc(vid):#sql injection 
	if(vid<0 or vid>9):raise Exception('vid out of range '+vid)
	vid=str(vid)
	sql='SELECT count(vid) FROM "v" where vid='+vid
	return exe(sql)[0][0]
	
def ip(aip):
	if(len(aip)<3):return False
	
	r=exe('''SELECT * FROM tip where ip='%s'  ;'''%aip)
	if(r==None or len(r)==0):
		exe('''insert into tip(ip) values('%s');'''%aip)
		return False
	else:
		
		return True
	# if()
	
try:
	execsql('''create table tip(ip INTEGER)''')

	execsql('''create table v(
	uid  INTEGER PRIMARY KEY,
	vid  INTEGER  NOT NULL,
	time INTEGER)''')
except:pass

print ip('aaa66a768568')
# execsql('insert into ta(t) values(1)')
# insert into v(vid) values(1)
# insert(1)
# vote(28)
# calc(1)