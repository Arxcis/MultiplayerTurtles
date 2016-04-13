#!/usr/bin/env python
# coding: utf-8

import turtle
from turtle import Turtle
from utils import bind_keys

import networks

players = {}
playerself = "green"

def setup():
    player_self = Turtle()
    bind_keys(player_self)
    turtle.listen()


def handle_create(playername):
    """
    Lag ny turtle og sett farge utifra playername.
    :param playername:
    :return:
    """
    players[playername] = Turtle()
    players[playername].color(playername)


def handle_remove(playername):
    """
    Lag ny turtle og sett farge utifra playername.
    :param playername:
    :return:
    """
    players[playername].clear()
    players[playername].ht()
    del(players[playername])


def handle_move(playername, direction):
    """
    Beveger turtle
    :param direction:
    :param playername:
    :return:
    """
    padde = players[playername]
    padde.seth(direction)
    padde.penup()
    padde.forward(50)


if __name__ == '__main__':

    setup()
    networks.register_handlers(handle_move, handle_create, handle_remove)
    networks.start(playerself)
    print("her")

    # networks.test_message()
    turtle.mainloop()
