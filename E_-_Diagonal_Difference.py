import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    
    for i in range(len(arr[0])):
        left_diagonal = left_diagonal + arr[i][i]
        right_diagonal = right_diagonal + arr[i][len(arr[0])-i-1]

    answer = abs(left_diagonal - right_diagonal)

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()