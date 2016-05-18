# https://codility.com/programmers/task/min_abs_sum_of_two/
import math

import sys
def solution(A):

    s = [a for a in A]

    s.sort()

    i = 0
    j = len(A) - 1

    minSum = sys.maxint

    while i <= j:
        minSum = min(minSum, abs(s[i]+s[j]))

        if abs(s[i]) > abs(s[j]):
            i += 1
        else:
            j -= 1

    return minSum








print solution([-8, 4, 5, -10, 3 ])
print solution([0])
print solution([2])
