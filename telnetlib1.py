

import getpass
import sys
import telnetlib

HOST = "192.168.0.106"
user = "admin"
password = "root@123"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(b"admin")

if password:
    tn.read_until(b"Password: ")
    tn.write(b"root@123")

tn.write(b"en")
tn.write(b"root@123")
tn.write(b"sh ip inter br")

print(tn.read_all())
