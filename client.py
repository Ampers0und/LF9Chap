#!/usr/bin/env python3

import hashlib
from xmlrpc import client
#from xmlrpc.client import ServerProxy as XMLServerProxy

username = 'Andi'
password = 'test'

s = client.ServerProxy('http://localhost:1337')
challenge = s.getchallenge(username)

print(challenge)

hashed_password = hashlib.sha512((password + str(challenge)).encode()).hexdigest()

print(s.login(username, hashed_password))
print(s.add(5,5))
