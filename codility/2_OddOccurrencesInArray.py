# https://codility.com/programmers/task/odd_occurrences_in_array/

def solution(A):

    # Solution 1: time O(nlogn), space 1

    A.sort()
    for i in range(1, len(A)-1, 2):
        if A[i] != A[i-1]:
            return A[i-1]

    return A[-1]

def best_solution(A) :

    # Runs on Space 1, time n, can be easily paralelized

    missing = 0

    for a in A:
        missing ^= a
    return a

if __name__ == '__main__':
    print solution([4,3,2,2,2,2,3])