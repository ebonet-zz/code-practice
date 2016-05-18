# https://codility.com/programmers/task/tie_ropes/


def solution(K, A):
    n = 0
    curLength = 0

    for a in A:
        if curLength +a >= K:
            curLength = 0
            n += 1
        else:
            curLength += a

    return n

print solution(4, [1, 2, 3, 4, 1, 1, 3])