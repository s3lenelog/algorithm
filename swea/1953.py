# bfs
# depth, 최단 거리
import copy

# stack 구현 생각해보기
up_matched      = [[],
                   [1,2,5,6],
                   [1,2,5,6],
                   [],
                   [1,2,5,6],
                   [],
                   [],
                   [1,2,5,6]]

down_matched    = [[],
                   [1,2,4,7],
                   [1,2,4,7],
                   [],
                   [],
                   [1,2,4,7],
                   [1,2,4,7],
                   []]

left_matched    = [[],
                   [1,3,4,5],
                   [],
                   [1,3,4,5],
                   [],
                   [],
                   [1,3,4,5],
                   [1,3,4,5]]

right_matched   = [[],
                   [1,3,6,7],
                   [],
                   [1,3,6,7],
                   [1,3,6,7],
                   [1,3,6,7],
                   [],
                   []]

bfs = []


def get_spot_count(c, start_row, start_col, visited, depth):
    global ternel, up_matched, down_matched, left_matched, right_matched, bfs
    # # 1. set visited
    # visited[start_row][start_col] = True
    # 1-2. root node push
    bfs.append((start_row, start_col, 1))

    while len(bfs):
        start_row, start_col, depth = bfs.pop(0)
        if visited[start_row][start_col]:       # 현재 노드 방문 여부 확인
            continue

        visited[start_row][start_col] = True    # 현재 노드 방문 체크
        
        if depth > L:
            continue
        
        # 가능한 공간 수 count
        c += 1
        
        # 다음 depth 설정을 위해 증가
        depth += 1
        
        # check => bfs queue append
        # - index range
        # - 연결?
        # - visited?
        # 2-1. up
        if start_row > 0 \
                and ternel[start_row-1][start_col] in up_matched[ternel[start_row][start_col]] \
                and not visited[start_row-1][start_col]:
            bfs.append((start_row-1, start_col, depth))     # bfs queue push

        # 2-2. down
        if start_row < N-1 \
                and ternel[start_row+1][start_col] in down_matched[ternel[start_row][start_col]]  \
                and not visited[start_row+1][start_col]:
            bfs.append((start_row+1, start_col, depth))

        # 2-3. left
        if start_col > 0 \
                and ternel[start_row][start_col-1] in left_matched[ternel[start_row][start_col]] \
                and not visited[start_row][start_col-1]:
            bfs.append((start_row, start_col-1, depth))

        # 2-4. right
        if start_col < M-1 \
                and ternel[start_row][start_col+1] in right_matched[ternel[start_row][start_col]] \
                and not visited[start_row][start_col+1]:
            bfs.append((start_row, start_col+1, depth))

    return c


T = int(input())

for test_case in range(1, T + 1):
    # 1. get ternel data ##################################
    # N total_row, M total_col, R hole_row, C hole_col, L time
    # (R, C) -> entry point
    N, M, R, C, L = [int(data) for data in input().split()]
    ternel = []
    bfs = []
    for row in range(N):
        ternel.append([int(r) for r in input().split()])
    
    count = 0
    # 2. find spots and get the count of the spots (get_spot_count)
    count = get_spot_count(count, R, C,  [[False] * M for i in range(N)], 0)

    # 3. print the count
    print(f'#{test_case} {count}')
