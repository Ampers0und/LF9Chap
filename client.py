#!/usr/bin/env python3

import hashlib
from xmlrpc import client
#from xmlrpc.client import ServerProxy as XMLServerProxy

username = 'Andi'
password = 'test'

s = client.ServerProxy('http://localhost:1337')
#Zieht sich das Salt für Chap
challenge = s.getchallenge(username)
token = ''

#Noch kein Token vorhanden
print(s.multiply(5,6,token))
print(challenge)
hashed_password = hashlib.sha512((password + str(challenge)).encode()).hexdigest()

if(s.login(username, hashed_password)):
    #erstellt erst bei erfolgreicher anmeldung ein UserToken 
    token = s.getToken(username)
print(s.add(5,5))
print(token)
print(s.multiply(5,6,token))
