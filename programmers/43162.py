# 코딩테스트 연습 - 깊이/너비 우선 탐색(DFS/BFS) - 네트워크
# dfs

def dfs(root, n, computers, visited):
    visited[root] = True
    for node in range(n):
        if root != node and not visited[node] and computers[root][node]:
            dfs(node, n, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for node in range(n):
        if visited[node]:
            continue
        answer += 1
        dfs(node, n, computers, visited)
    return answer
