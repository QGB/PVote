types='''html,htm,png,jpg,js,css,ttf,woff,cur'''.split(',')
#cur got problem
from extended_BaseHTTPServer import serve,route,redirect,override
from qgb import U,T
import os,sys;basedir=os.path.dirname(__file__)
@route("/",["GET"])
def index(**kwargs):
	return redirect('/DEMO.html')
	
@route("/r",["GET",'POST'])
def r(location="http://baidu.com"):
	return {"content":"","code":301,"Location":location}

@route("/vote",["GET",'POST'])
def b(id='Error!'):
	return {
	"content":U.read(basedir+'/bg.jpg','rb'),
	"code":235,
	"Cache-Control":"no-cache"
	}	
sfr='''
@route("/{0}",["GET"])
def {1}():
	return {{
	"content":U.read(basedir+'/{0}','rb'),
	"code":235,
	"Cache-Control":"no-cache"
	}}
'''
def search(path):
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp):
			for i in types:
				if filename.endswith('.'+i):
					filename=T.sub(fp,basedir,'')[1:].replace('\\','/')
					funcname='fr_'+T.varname(filename)
					exec(sfr.format(filename,funcname))
					print filename,funcname
					break
		elif os.path.isdir(fp):
			search(fp)
search(basedir)

# U.x()
ip="0.0.0.0";port=80
U.pln(ip,port)
serve(ip,port)