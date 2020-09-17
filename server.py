#!/usr/bin/env python3

import random
import hashlib
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("0.0.0.0", 1337), requestHandler=RequestHandler)
server.register_introspection_functions()

class UserConn:

	username = ''
	password = ''
	loggedIn = False
	challenge = 0
	
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def generate_challenge(self):
		self.challenge = random.randrange(1000000,9999999)
		return self.challenge
	
	def login(self, u, h):
		if self.challenge == 0:
			return False
		hashed_password = hashlib.sha512((self.password + str(self.challenge)).encode()).hexdigest()
		self.loggedIn = h == hashed_password
		
		if (self.loggedIn):
			server.register_function(add)
		return self.loggedIn

userList = dict({"Andi": UserConn("Andi", "test"), "Felix": UserConn("Felix", "test2")})

def add(a,b):
	return a + b

def getchallenge(username):
	if username in userList:
		return userList[username].generate_challenge()
	return 0

def login(username, hash):
	if username in userList:
		return userList[username].login(username, hash)
	return False

server.register_function(getchallenge)
server.register_function(login)

server.serve_forever()
