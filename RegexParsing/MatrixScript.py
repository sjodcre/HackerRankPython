#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
final = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    # print([matrix[n][i] for n in range(n)])
    final.append([matrix[n][i] for n in range(n)])
# print( ''.join( ''.join(s) for s in final ))
print(re.sub(r"(?<=[a-zA-Z])(\W+)(?=[a-zA-Z])", " ", ''.join( ''.join(s) for s in final )))