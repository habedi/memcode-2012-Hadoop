#!/usr/bin/env python

import sys

c = 0
for x in sys.stdin:
    if not ('@' in x or '+' in x) :
        print '%s:%s' % (c,x.replace("\n",""))
        c += 1
    pass
