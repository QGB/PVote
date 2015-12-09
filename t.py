from qgb import U,T,Clipboard
from time import time,sleep
import urllib2
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
for i in range(9999):
	Thread(target=ta,args=[i]).start()
# ta()