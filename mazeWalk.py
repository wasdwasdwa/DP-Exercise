arr = [[1,3,1],[1,5,1],[4,2,1]]
dp = arr.copy()
for i in range(1,len(dp)):
    dp[i] = [float('inf')]*len(dp[i])
dp[0][0] = arr[0][0]
m=3
n=3
#第一列先弄出来
for x in range(1,n):
    dp[x][0] = min(dp[x][0], arr[x][0] + dp[x - 1][0])

#每一行往右
for x in range(n):
    curr_x = x
    curr_y = 1
    while curr_y< m:
        dp[curr_x][curr_y] = dp[curr_x][curr_y-1] + arr[curr_x][curr_y]
        curr_y += 1
        
#从第二列开始往下
for y in range(1, m):
    curr_x = 1
    curr_y = y
    while curr_x<n:
        dp[curr_x][curr_y] = min(dp[curr_x][curr_y],dp[curr_x-1][curr_y]+arr[curr_x][curr_y])
        curr_x += 1

print(dp)


