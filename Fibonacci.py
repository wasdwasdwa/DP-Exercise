#递归
def fib1(n):
    if n == 1 or n == 2:
        return 1
    re = fib1(n-1)+fib1(n-2)
    return re


#dp
def fib2(n):
    dp = [0]*n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]


print(fib1(8))
print(fib2(8))
