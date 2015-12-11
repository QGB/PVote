from qgb import U,T,Clipboard
import os,sys;basedir=os.path.dirname(__file__)

path=basedir+'''\DEMO_files'''
sfd=basedir+'/vote.html'
sd=U.read(sfd)
for f in os.listdir(path):
	if not f.endswith('jpg'):continue
	# if :continue
	i=-1
	try:i=int(f[:1])
	except:continue
	sd=sd.replace(f[1:],f)
	# print f
print sd
U.write(sfd,sd)
U.x()