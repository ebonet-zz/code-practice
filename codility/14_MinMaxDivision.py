# https://codility.com/programmers/task/min_max_division/

# Step 1: given a maxSum, compute how many blocks are needed
# to split the array so that the sum of each block is less than
# maxSum

def blocks_needed(A, maxSum):
    blocks = 1
    curr_block = 0
    for a in A:
        if curr_block + a > maxSum:
            curr_block = a
            blocks += 1
        else:
            curr_block += a

    return blocks

# Step 2: Perform binary search. At each step, we check if
# given the maxSum the number of blocks need is less than
# the available blocks. If the number of blocks is less, we
# try a smaller maxSum. If it is greater, we try a bigger maxSum

def solution(K, M, A):

    top = sum(A)
    bottom = max(A)

    if K==1:
        return top
    if K >= len(A):
        return bottom


    result = 0
    while top >= bottom:
        mid = (top+bottom) / 2

        n_blocks = blocks_needed(A, mid)

        if n_blocks <= K:
            top = mid-1
            result = mid
        else:
            bottom = mid+1

    return result

print(solution(3, 6, [5, 2, 3, 4, 6]))
