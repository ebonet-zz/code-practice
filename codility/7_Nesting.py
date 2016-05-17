# https://codility.com/programmers/task/nesting/

def solution(s):

    stack = 0

    for st in s:
        stack += 1 if st == '(' else -1

        if stack < 0:
            return False

    return stack == 0


print(solution(""))
print(solution("()"))
print(solution(")"))
print(solution("("))
print(solution("(())()"))