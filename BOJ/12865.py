# Q. 12865
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
items = [(0, 0)] + items

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= items[i][0]:  # j가 item 무게 이상이라면!
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]] + items[i][1]])   # i번째 item 안 넣었을 때 값과, 넣었을 때 값 계산! 
        else:  # i번째 item도 넣을 수 있는 것
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k])