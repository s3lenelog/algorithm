# 디저트 카페 
# dfs
# SWEA 댓글과 아래 블로그 참고해서 해결함.
# https://bloodstrawberry.tistory.com/256

import copy
import time 

# down-left | down-right | up-right | up-left 순서로 확인. (시계방향)
row_dir = [1, 1, -1, -1]
col_dir = [-1, 1, 1, -1]

def dfs(r, c, visited, types, dir):
    global area, max_dessert, max_types, N
    visited[r][c] = True
    types.append((r, c, area[r][c]))

    # (dir == 3) & 루트 노드와 동일한 위치이면 
    # 디저트 수가 최대인지 확인 -> 맞으면 max_dessert update, 아니면 return
    if dir == 3 and types[0][0] == r and types[0][1] == c:
        if len(types) - 1 > max_dessert:
            max_dessert = len(types) - 1
            #print(f'[O] Changed max_dessert :: {max_dessert}')
            visited[r][c] = False
            types.pop()
            return
        else:
            visited[r][c] = False
            types.pop()
            return

    # 원래 가던 방향 체크
    if (r + row_dir[dir] < N and r + row_dir[dir] >= 0) \
        and (c + col_dir[dir] < N and c + col_dir[dir] >= 0) \
        and ((not visited[r + row_dir[dir]][c + col_dir[dir]] \
        and area[r + row_dir[dir]][c + col_dir[dir]] not in [t[2] for t in types]) \
             or (types[0][0] == r + row_dir[dir] and types[0][1] == c + col_dir[dir])):  # 다음 노드 루트인지 체크
        dfs(r + row_dir[dir], c + col_dir[dir], visited, types, dir)

    # 시계 방향 체크
    if dir < 3 \
            and r + row_dir[dir + 1] < N and r + row_dir[dir + 1] >= 0 \
            and c + col_dir[dir + 1] < N and c + col_dir[dir + 1] >= 0 \
            and ((not visited[r + row_dir[dir + 1]][c + col_dir[dir + 1]] \
            and area[r + row_dir[dir + 1]][c + col_dir[dir + 1]] not in [t[2] for t in types]) \
                or (types[0][0] == r + row_dir[dir+1] and types[0][1] == c + col_dir[dir+1])):
        dfs(r + row_dir[dir + 1], c + col_dir[dir + 1], visited, types, dir + 1)

    visited[r][c] = False  # 방문 후에 다른 루트도 방문해야 하므로 visited False로 세팅 & types.pop()
    types.pop()

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # area size
    max_dessert = -1
    area = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]  # area visited

    # area의 각 위치마다 dfs() 호출하여 최대 디저트 수 확인
    for row in range(N):
        for col in range(N):
            visited = [[False] * N for _ in range(N)]
            dfs(row, col, visited, [], 0)

    print(f'#{test_case} {max_dessert}')
