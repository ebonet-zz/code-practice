# https://codility.com/programmers/task/stone_wall/

def solution(H):
    b_stack = []

    n_blocks = 0

    for h in H:
        while b_stack and h < b_stack[-1]:
            b_stack.pop()
            n_blocks += 1

        if not b_stack or h > b_stack[-1]:
            b_stack.append(h)

    return n_blocks+len(b_stack)
#
# print solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
# print solution([1,0,1])
# print solution([0,0,0])
print solution([2, 5, 1, 4, 6, 7, 9, 10, 1])