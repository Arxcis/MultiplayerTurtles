#!/usr/bin/env python
# coding: utf-8


from protocol import CREATE, MOVE, REMOVE
from socket import socket
import threading
s = socket()
playerself = None

handlers = []

def start(name):
    global playerself
    playerself = name
    t = threading.Thread(target=listen_to_server)
    t.start()



def register_handlers(*args):
    handlers = args


def send_message(msg):
    """
    Sender beskjed til server
    :param msg:
    :return:
    """
    s.send(msg.encode(encoding='utf-8'))


def handle_received_message(msg):
    """
    Tolker beskjed fra server og utføre en handling etter protokoll
    :param msg:
    :return:
    """

    # message parts
    parts = msg.split(',')
    cmd = parts[0]
    playername = parts[1]

    if cmd == 'create':
        handlers[1](playername)

    if cmd == 'remove':
        handlers[2](playername)

    if cmd == 'move':
        direction = int(parts[2])
        handlers[0](playername, direction)




def listen_to_server():
    print ("Started the thread")
    ip = '10.72.32.230'
    port = 1337

    s.connect((ip, port))
    print ("connected to server", ip, port)
    send_message(CREATE(playerself))
    while True:
        message = s.recv(1024).decode(encoding='utf-8')
        handle_received_message(message)


def test_message():
    """
    Teste om network funker
    :return:
    """
    handle_received_message("create,green")
    handle_received_message("move,green,90")
    import time
    time.sleep(2)
    handle_received_message("remove,green")

def test_socket():
    send_message("create,green")