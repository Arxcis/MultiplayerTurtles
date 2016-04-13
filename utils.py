#!/usr/bin/env python
# coding: utf-8

import turtle
import networks
from protocol import MOVE, REMOVE, CREATE

def bind_keys(player):
    """
    :param player:
    :return:
    """

    def up():
        player.seth(90)
        player.fd(50)
        networks.send_message(MOVE("green", 90))

    def down():
        player.seth(270)
        player.fd(50)

    def right():
        player.seth(0)
        player.fd(50)

    def left():
        player.seth(180)
        player.fd(50)

    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')