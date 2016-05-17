# https://codility.com/programmers/task/perm_missing_elem/

def solution(A):

    greater = 0
    lenA = len(A)
    N = lenA + 1
    i = 0

    while i < lenA:

        if A[i] == i + 1 or A[i] == N:
            i += 1
            continue

        A[A[i]-1], A[i] = A[i],A[A[i]-1]


    for i in xrange(lenA):
        if i + 1 != A[i]:
            return i + 1
    return N

print solution([2,1,3,5])
print solution([])
print solution([1,2,3,4])
print solution([4, 2, 3, 5, 1, 6, 8, 9])
