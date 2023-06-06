#!/usr/bin/env python

def knapSack(W, data):
    n=len(data.keys())
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    dict2tuple = tuple(data.items())
    for i in range(n + 1):
        for j in range(W + 1):
            curVal = dict2tuple[i-1][1][0]
            curWt = dict2tuple[i-1][1][1]
            if i == 0 or j == 0:
                table[i][j] = 0
            elif curWt <= j:
                table[i][j] = max(curVal + table[i-1][j-curWt], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
                print(f">=====>> {dict2tuple[i-1][0]} <<====<")
    [print(x) for x in table]
    return table[n][W]

ks_data = {'a': (1, 1), 'b': (1, 2), 'c': (1, 3), 'd': (1, 4), 'e': (1, 5), 'f': (1, 2), 'g': (1, 3), 'h': (1, 1), 'i': (1, 3), 'j': (1, 1), 'k': (1, 1), 'l': (1, 1), 'm': (1, 3), 'n': (1, 2)}
print(knapSack(15, ks_data))