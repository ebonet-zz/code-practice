# https://codility.com/programmers/task/frog_jmp/
import math


def solution(x,y,d):
    return int(math.ceil((float(y-x)/d)))

if __name__ == '__main__':
    print solution(10,40,10)
    print solution(5, 105, 3)