import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] < 0:
            minus += 1
        else:
            plus += 1

    len_arr = len(arr)
    minus_fraction = float(minus)/float(len_arr)
    plus_fraction = float(plus) / float(len_arr)
    zero_fraction = float(zero) / float(len_arr)
    print(plus_fraction)
    print(minus_fraction)
    print(zero_fraction)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)