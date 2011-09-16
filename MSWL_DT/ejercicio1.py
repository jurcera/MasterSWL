#!/usr/bin/env python

f = open('/etc/passwd','r')
lineas = f.readlines()
for linea in lineas:
    elemento = linea.split(':')
    print elemento[0]+' -> '+elemento[6].rstrip('\n')
f.close
