#!/usr/bin/env python
# coding: utf-8


from socket import socket
import threading

s = socket()


def start_listen_thread(container):
    t = threading.Thread(target=listen_to_server, args=(container, ''))
    t.start()


def listen_to_server(container, tom):
    print ("Started the thread")

    name, handler, protocol = container
    ip = '127.0.0.1'
    port = 1337

    s.connect((ip, port))
    send_message(protocol.CREATE(name))
    while True:
        message = s.recv(1024).decode(encoding='utf-8')
        if message:
            handler.handle_received_message(message)


def send_message(msg):
    """
    Sender beskjed til server
    :param msg:
    :return:
    """
    s.send(msg.encode(encoding='utf-8'))






"""
def test_message():
    Teste om network funker
    :return:
    handle_received_message("create,green")
    handle_received_message("move,green,90")
    import time
    time.sleep(2)
    handle_received_message("remove,green")

def test_socket():
    send_message("create,green")
"""
