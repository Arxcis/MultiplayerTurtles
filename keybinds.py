#!/usr/bin/env python
# coding: utf-8

import networks

def bind_keys(player, protocol, screen):

    def up():
        networks.send_message(protocol.MOVE(player, 90))

    def down():
        networks.send_message(protocol.MOVE(player, 270))

    def right():
        networks.send_message(protocol.MOVE(player, 0))

    def left():
        networks.send_message(protocol.MOVE(player, 180))

    screen.onkey(left, 'Left')
    screen.onkey(right, 'Right')
    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')