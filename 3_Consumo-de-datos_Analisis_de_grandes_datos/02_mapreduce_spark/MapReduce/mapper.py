#!/usr/bin/env python3

from sys import stdin

for line in stdin:
    vals = line.split(",")
    profit = float(vals[9]) - float(vals[10])
    state = vals[8]
    print(state, "\t", profit)
