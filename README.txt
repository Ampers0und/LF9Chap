
1. 	Für die Programme wird Python3, sowie die folgenden Dependencies benötigt :
		- random
		- hashlib
		- string
		- xmlrpc.server.SimpleXMLRPCServer 
		- xmlrpc.server.SimpleXMLRPCRequestHandler
		- xmlrpc.client


2. 	Rufen sie die Programme mit dem Python-Befehl mittels eines eindeutigen Pfades auf.

		Bsp.:

		"python [C:\User\[Name]\Downloads]\client.py"
		"python [C:\User\[Name]\Downloads]\server.py"

3. 	Beim Starten sieht man, dass vor dem Log-In einmal versucht wird die Multiply-Funktion aufzurufen, 
	jedoch ist das nicht möglich, da der User noch nicht eingeloggt ist.
	Danach findet automatisch der Log-In statt.
	Sobald man eingeloggt ist, kann man mittels des Befehls "s.multiply()" die Multiply-Funktion erneut aufrufen.
	Da man jetzt eigeloggt ist, sollte der Funktions-Aufruf nun funtionieren.
	
