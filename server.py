
import socketserver
from socket import socket

clients = []

def relay(msg):
    for client in clients:
        client.request.send(msg)

class ClientHandler(socketserver.BaseRequestHandler):
    """ Denne class-en har kun 1 metode: "def handle(self)".
          Metoden "handle" blir bare kjørt FØRSTE gang clienten
           snakker med serveren."""

    def handle(self):
        # Store new ClientRequest-object in list of client-objects.
        clients.append(self)
        # 
        while 1:
            data = self.request.recv(1024)
            if data:
                relay(data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ ------------- 2--1 CLASS ---------------------
    For å lage en TCPServer som i tillegg kan bruke "threading", 
     så lager vi en ny klasse, som BARE har som oppgave å spleise 
      de 2 klassene den arver fra.
       
    | SocketServer.ThreadingMixIn + SocketServer.TCPServer = Sant!<3 |
    |       Class 1               +     Class 2          = UBERClass |
    """
    pass


if __name__ == "__main__":
    HOST, PORT = "192.168.1.10", 1337

    # Create the server, binding to server-IP on port 1337
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()