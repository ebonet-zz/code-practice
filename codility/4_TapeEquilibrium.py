#https://codility.com/programmers/task/tape_equilibrium/
import sys
import math


def solution(A):

    minValue = sys.maxint
    leftSum = A[0]
    rightSum = sum(A)-A[0]

    for i in xrange(1, len(A)):
        minValue = min(minValue, math.fabs(leftSum - rightSum))

        leftSum += A[i]
        rightSum -=A[i]

    return int(minValue)


print solution([3,1,2,4,3])
print solution([3])
print solution([-1000, 1000])
