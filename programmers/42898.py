# 프로그래머스 - DP
# 등굣길

import copy
import sys

def solution(m, n, puddles):
    answer = 0
    
    # init dp
    dp = [copy.deepcopy([0]*m) for _ in range(n)]
    dp[0][0] = 1
    for c, r in puddles:
        dp[r - 1][c - 1] = -1
    
    for row in range(n):
        for col in range(m):
            if dp[row][col] < 0:
                continue
                
            # right
            if col + 1 < m and dp[row][col + 1] > -1:
                dp[row][col + 1] += dp[row][col]

            # down
            if row + 1 < n and dp[row + 1][col] > -1:
                dp[row + 1][col] += dp[row][col]
                
    answer = dp[n - 1][m - 1] % 1000000007
    return answer
