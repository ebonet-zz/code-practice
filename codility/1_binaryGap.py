# https://codility.com/programmers/task/binary_gap/

def binaryGap(N):
    n = N
    maxGap = 0
    curGap = 0
    is_counting = False
    while n != 0:

        if n % 2 == 1:
            maxGap = max(maxGap, curGap)
            curGap = 0
            is_counting = True

        elif is_counting :
            curGap += 1

        n  = int(n/2)

    return maxGap


if __name__ == '__main__':
    print binaryGap(9)
    print binaryGap(529)
    print binaryGap(20)
    print binaryGap(15)