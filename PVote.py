# -*- coding: utf-8 -*- 
types='''html,htm,png,jpg,js,css,ttf,woff,cur'''.split(',')
#cur got problem
from extended_BaseHTTPServer import serve,route,redirect,override
from qgb import U,T
import os,sys;basedir=os.path.dirname(__file__)
simgfolder='DEMO_files'
gysimg=[]
def getpath(id):
	for i in gysimg:
		if i[:1]==str(id):
			return '/'+simgfolder+'/'+i
			
def getdes(id):
	for i in gysimg:
		if i[:1]==str(id):
			return i[1:][:-4]
	
@route("/",["GET"])
def index(**kwargs):
	return redirect('/DEMO.html')
	
@route("/result",["GET"])
def result(id='9'):#必须提供默认参数，否则服务器内部错误，，，在隐身模式下表现最好
	try:
		id=id[0]
		sid=int(id)+1;sid=str(sid)
		sr=U.read(basedir+'/result.html')
		# sr=sr.replace('{id}',sid)
		# sr=sr.replace('{img}',getpath(id))
		# sr=sr.replace('{des}',getdes(id))
	except Exception as e:sr=e
	# sr='6543'
	return {
	"content":sr,
	"code":235,
	"Cache-Control":"no-cache"
	}	
########################################
@route("/vote",["GET",'POST'])
def vote(id='Error!'):
	id=id[0]
	sid=int(id)+1;sid=str(sid)
	####  Vote logic####
	
	####################
	sv=U.read(basedir+'/vote.html')
	try:
		sv=sv.replace('{id}',sid)
		sv=sv.replace('{img}',getpath(id))
		sv=sv.replace('{des}',getdes(id))
	except Exception as e:sv=e
	
	return {
	"content":sv,
	"code":235,
	"Cache-Control":"no-cache"
	}	
sfr='''
@route("/{0}",["GET"])
def {1}():
	sc="no-cache"
	icode=235
	if '{0}'.endswith('bg.jpg'):sc='max-age='+str(60*10)#增加读取文件判断有问题，复杂度提升
	return {{
	"content":U.read(basedir+'/{0}','rb'),
	"code":icode,
	"Cache-Control":sc
	}}
'''
def search(path):
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp):
			for i in types:
				if filename.endswith('.'+i):
					if filename.endswith('jpg') and filename[:1] in '1,2,3,4,5,6,7,8,9,0'.split(','):
						if filename not in gysimg:gysimg.append(filename)
				
					filename=T.sub(fp,basedir,'')[1:].replace('\\','/')
					funcname='fr_'+T.varname(filename)
					exec(sfr.format(filename,funcname))
					print filename,funcname
					break
		elif os.path.isdir(fp):
			search(fp)
search(basedir)

# print gysimg
# print getpath(1),getdes(5)
# U.x()

ip="0.0.0.0";port=80
U.pln(ip,port)
serve(ip,port)