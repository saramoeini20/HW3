#!/usr/bin/python3
# -*-coding:utf-8 -*

import sys
import collections
total = 0
lastword = None

cn = collections.Counter()
for line in sys.stdin:
    line = line.strip()
    word, count = line.split()
    count = int(count)
    if lastword is None:
        lastword = word
    if word == lastword:
        total += count
    else:
        #print("%s\t%d" % (lastword, total))
        cn[lastword] += total
        total = count
        lastword = word

if lastword is not None:
    #print("%s\t%d" % (lastword, total))
    cn[lastword] += total

print("most frequences are:")
print(cn.most_common(10))