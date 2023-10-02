import copy

def solution(triangle):
    answer = 0
    dp = [copy.deepcopy([0] * len(triangle)) for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for row in range(0, len(triangle) - 1):
        for col in range(row+1):
            if dp[row + 1][col] < dp[row][col] + triangle[row + 1][col]:
                dp[row + 1][col] = dp[row][col] + triangle[row + 1][col]
            if dp[row + 1][col + 1] < dp[row][col] + triangle[row + 1][col + 1]:
                dp[row + 1][col + 1] = dp[row][col] + triangle[row + 1][col + 1]
    
    answer = max(dp[len(dp) - 1])

    return answer
