# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
# bfs : dfs로 풀이 시 모든 경로 탐색으로 시간 복잡도에서 불리.

# 정확성 테스트 pass
# 효율성 테스트 fail
def dfs(root, maps, depth, visited, result):
    row, col = root
    depth += 1
    visited[row][col] = True
    
    
    # up
    if row > 0 and maps[row-1][col] and not visited[row-1][col]:
        dfs((row-1, col), maps, depth, visited, result)
    
    # down
    if row < len(maps) - 1 and maps[row+1][col] and not visited[row+1][col]:
        dfs((row+1, col), maps, depth, visited, result)
    
    # left
    if col > 0 and maps[row][col-1] and not visited[row][col-1]:
        dfs((row, col-1), maps, depth, visited, result)
    
    # right
    if col < len(maps[0]) - 1 and maps[row][col+1] and not visited[row][col+1]:
        dfs((row, col+1), maps, depth, visited, result)
    
    if row == len(maps) - 1 and col == len(maps[0]) - 1:
        print(root)
        result.append(depth)
        visited[row][col] = False
        depth -= 1
        return
    
    depth -= 1
    visited[row][col] = False
    
    
def solution_dfs(maps):
    answer = -1
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    result = []
    
    dfs((0,0), maps, 0, visited, result)
    
    if len(result):
        answer = min(result)
    
    return answer

# 효율성, 정확성 테스트 모두 pass
def bfs(maps):
    q = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    q.append((0, 0, 0))    
    
    while len(q):
        row, col, depth = q.pop(0)
        if visited[row][col]: continue
        depth += 1
        visited[row][col] = True

        # queue에 저장 -> 가장 먼저 발견한 경우의 수가 최단거리
        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            return depth
        
        # up
        if row > 0 and maps[row-1][col] and not visited[row-1][col]:
            q.append((row-1, col, depth))

        # down
        if row < len(maps) - 1 and maps[row+1][col] and not visited[row+1][col]:
            q.append((row+1, col, depth))

        # left
        if col > 0 and maps[row][col-1] and not visited[row][col-1]:
            q.append((row, col-1, depth))

        # right
        if col < len(maps[0]) - 1 and maps[row][col+1] and not visited[row][col+1]:
            q.append((row, col+1, depth))

    return -1
        
    
def solution(maps):
    answer = 0
    answer = bfs(maps)
    return answer
