#!/usr/bin/env python
# coding: utf-8

class NetworkProtocol:

    def MOVE(self, playername, direction):
        return 'move,%s,%s' % (playername, direction)

    def CREATE(self, playername):
        return 'create,%s' % (playername)

    def REMOVE(self, playername):
        return 'remove,%s' % (playername)

