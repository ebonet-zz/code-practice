

# https://codility.com/programmers/task/common_prime_divisors/
def solution(A, B):

    def gcd(a, b):
        return b if not a % b else gcd(b, a % b)

    ## Factor the divisors out. the gcd contains all commn divisors
    ## If the number has factors outside of the common set, it return
    ## a value different than one
    def remove_prime_divisors(x, divisors):
        while x != 1:
            g = gcd(x, divisors)

            ## No more divisors
            if g == 1:
                break

            x /= g
        return x

    def has_same_divisors(x,y):

        g = gcd(x, y)

        if remove_prime_divisors(x, g) != 1 or remove_prime_divisors(y,g) != 1:
            return 0
        return 1

    return sum(has_same_divisors(a,b) for a,b in zip(A,B))

# Cases to test: [1,1], [2,1], [2,2], [5,3], [36,24]


print(solution([15, 10, 3, 36, 2], [75, 30, 5, 24, 2]))
# print(solution([2],[2]))