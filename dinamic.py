import time

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib (n - 2)
#
#
# t0 = time.clock()
# k = fib(50)
# t1 = time.clock()
#
# print (t1 - t0)

def num_digits(n):
    count = 0
    while n > 0:
        if n == 0:
            count += 1
        count += 1
        n = n/10

    return count

def fibM(n):
    memo = {}
    def fib(n):
        if n==1:
            return 0
        if n==2:
            return 1
        if(n-2) not in memo:
            memo[n-2] = fib(n-2)
        if(n-1) not in memo:
            memo[n-1] = fib(n-1)
        return memo[n - 1] + memo[n - 2]
    return fib(n)

def fib(n):
    if n==0:
        return 0
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


t0 = time.clock()
k = fib(10000)
print
t1 = time.clock()



print k
print num_digits(k)
print (t1 - t0)
