#!/usr/bin/env python3

import random
import hashlib
import string
import random

#Simple Funktion zum Generieren von Zufallszahlen
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("0.0.0.0", 1337), requestHandler=RequestHandler)
server.register_introspection_functions()

#Speichert User Session Tokens
tokenList = [];

class UserConn:

    username = ''
    password = ''
    loggedIn = False
    challenge = 0
    token = ''
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generate_challenge(self):
        #Salt wird pro User generiert und an User beim Login mitgegeben
        self.challenge = random.randrange(1000000,9999999)
        return self.challenge

    def generate_token(self):
        #wird erst bei erfolgreichem Login ausgeführt
        self.token = id_generator()
        tokenList.append(self.token)
        return self.token
    
    def login(self, u, h):
        if self.challenge == 0:
                    return False
        hashed_password = hashlib.sha512((self.password + str(self.challenge)).encode()).hexdigest()
        self.loggedIn = h == hashed_password
        
        if (self.loggedIn):
            #sobald ein User eingeloggt ist wird Funktion für alle freigeschaltet
            server.register_function(add)
        return self.loggedIn

#Liste mit registrierten Benutzern
userList = dict({"Andi": UserConn("Andi", "test"), "Felix": UserConn("Felix", "test2")})

def add(a,b):
    return a + b

def multiply(a,b,token):
    #Diese Funktion ist premium und nur als angemeldeter User aufrufbar
    if (token in tokenList):
        return a * b
    return 'not authenticated'

def getchallenge(username):
    #Vom Client aufrufbar, überprüft Username aus Dictionary
    if username in userList:
        return userList[username].generate_challenge()
    return 0

def getToken(username):
    #Das Gleiche wie oben, generiert Session token
    if username in userList:
        return userList[username].generate_token()
    return 0

def login(username, hash):
    if username in userList:
        return userList[username].login(username, hash)
    return False

server.register_function(getchallenge)
server.register_function(multiply)
server.register_function(getToken)
server.register_function(login)

server.serve_forever()
