import urllib2,os,sys
sys.path.append('C:\\PVote\\')
from qgb import U,T,Clipboard
from time import time,sleep


exec('''if 'a' not  in dir():a=32''')
print a
U.x()
def search(path):
	for filename in os.listdir(path):
		print filename

search('.')
U.x()


def ta(i=0):
	i=str(i)
	t=time()
	try:urllib2.urlopen('http://127.0.0.1:804?q='+i).read()
	except Exception as e:
		U.msgbox(U.ct())
		print e
	t=time()-t
	U.pln(t)

from threading import Thread
# for i in range(9999):
	# Thread(target=ta,args=[i]).start()
# ta()

import sqlite
# for i in range(77):
	# sqlite.exe('insert into v(vid) values(1)')
# sqlite.exe('65343f2')
def s(adict):
	items = adict.items()
	items.sort()
	return [value for key, value in items]
	
d={}
for i in range(7):
	d[i]=i*i-5*i

print d ,type(d)
d=U.sortDictV(d)	

for k,v in d:
	print k
# print d[0]
U.x()

print d ,type(d)