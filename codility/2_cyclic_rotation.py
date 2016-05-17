def solution(A,n):
    if not A:
        return A

    n = n % len(A)
    return A[len(A)-n:len(A)]+A[0 : (len(A)-n)]

if __name__ == '__main__':
    print solution([1,2,3], 1)
    print solution([], 1)
    print solution([1,2,3], 5)
    print solution([1,2,3], 4)
