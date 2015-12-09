from extended_BaseHTTPServer import serve,route,redirect,override
from qgb import U,T

@route("/",["GET"])
def index(**kwargs):
	return str(kwargs)

	if "name" in kwargs:
		return "Bonjour {0} <br /> <a href='/redirect'>Retour</a>".format(kwargs["name"][0])
	else:
		return "Index <br /> <a href='/?name=valentin'>Test Valentin</a><br /> <a href='/form'>Form Test</a>"
	
	
@route("/r",["GET",'POST'])
def r(location="http://baidu.com"):
	return {"content":"","code":301,"Location":location}

@route("/b",["GET",'POST'])
def b(location="http://baidu.com"):
	return {
	"content":"765432",
	"code":235,
	"Location":location,
	"Cache-Control":"no-cache"
	}


ip="0.0.0.0";port=804
U.pln(ip,port)
serve(ip,port)