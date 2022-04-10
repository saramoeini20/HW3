#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

for line in sys.stdin:
    line = line.strip()
    words = [w for w in line.split()]

    for word in words:
        print("%s\t%d" % (word, 1))