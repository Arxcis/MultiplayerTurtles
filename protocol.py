#!/usr/bin/env python
# coding: utf-8


def MOVE(playername, direction):
    return 'move,%s,%s' % (playername, direction)

def CREATE(playername):
    return 'create,%s' % (playername)

def REMOVE(playername):
    return 'remove,%s' % (playername)
