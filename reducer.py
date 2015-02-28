#!/usr/bin/python 

import hashlib

###############################################################
def pasreFASTQ(fname='/home/raziel/meWorkspace/Memcode-2012/2012-memocode-contest/DONE2/short_reference.fasta',bucket=100):
    fasta = open(fname,"r")
    l = []
    data = ''
    for i in fasta.readlines():
        if (i.strip() != '') and not '>' in i:
            data += i.replace("\n","")
            pass
    i = 0
    x = len(data)
    while((i+bucket) < x):
        hash_object = hashlib.md5(data[i:(bucket+i)])
        l.append(hash_object.hexdigest())
        i += 1
        pass
    return l
###############################################################
def findOccurrences(substr,ldata):
    hash_object = hashlib.md5(substr)
    substr = hash_object.hexdigest()
    occurrences = []
    pos = 0
    for i in ldata:
        if substr == i:
            occurrences.append(pos)
            pass
        pos += 1
        pass
    return occurrences
###############################################################
import sys

for line in sys.stdin:
    line = line.strip()
    try:
      x = line.split(":")
      if len(x) >= 2:
          print x[0],": ",findOccurrences(x[1],pasreFASTQ())
      pass
    except Exception:
	        # ignore/discard this line
      pass
##############################################################
