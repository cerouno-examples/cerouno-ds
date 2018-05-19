#!/usr/bin/env python3

from sys import stdin

prev = None
profit_sum = 0.0
for line in stdin:
    state, profit = line.split("\t")
    profit = float(profit)
    if prev and prev != state:
        print(prev, "\t", round(profit_sum, 2))
        profit_sum += 0
    profit_sum += profit
    prev = state
print(prev, "\t", round(profit_sum, 2))
