#!/usr/bin/env python
# coding: utf-8

# Standard
from turtle import Turtle, Screen

# Lokale moduler
from keybinds import bind_keys
from protocol import NetworkProtocol
import networks

screen = Screen()
players = {}
playerself = "green"


class Handler:

    def handle_received_message(self, msg):
        """
        Tolker beskjed fra server og utføre en handling etter protokoll
        :param msg:
        :return:
        """
        parts = msg.split(',')
        cmd = parts[0]
        playername = parts[1]

        if cmd == 'create':
            self.create(playername)

        if cmd == 'remove':
            self.remove(playername)

        if cmd == 'move':
            direction = int(parts[2])
            self.move(playername, direction)

    def create(self, playername):
        """
        Lag ny turtle og sett farge utifra playername.
        :param playername:
        :return:
        """
        players[playername] = Turtle()

        padde = players[playername]
        padde.color(playername)
        padde.shape("turtle")
        padde.penup()

    def remove(self, playername):
        """
        Fjern turtle 
        :param playername:
        :return:
        """
        padde = players[playername]
        padde.clear()
        padde.ht()

        del(players[playername])

    def move(self, playername, direction):
        """
        Beveger turtle
        :param direction:
        :param playername:
        :return:
        """
        padde = players[playername]
        padde.seth(direction)
        padde.forward(50)


def setup():
    # Setup objects
    players[playerself] = Turtle()
    handler = Handler()
    protocol = NetworkProtocol()

    # Setup keybinds
    bind_keys(playerself, protocol, screen)
    screen.listen()

    # Setup network listening
    container = [playerself, handler, protocol]
    networks.start_listen_thread(container)

if __name__ == '__main__':

    setup()
    screen.mainloop()
