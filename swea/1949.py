# 1949. [모의 SW 역량테스트] 등산로 조성
import copy

max_depth = 0

# 상하좌우
dir_row = [-1, 1, 0, 0]
dir_col = [0, 0, -1, 1]

def dfs(r, c, visited, depth, fixed):
    global N, K, area, max_depth

    visited[r][c] = True
    depth += 1

    # 상하좌우 확인
    for dir_idx in range(4):
        # index 범위 확인, visited 확인
        if r + dir_row[dir_idx] >= 0 and r + dir_row[dir_idx] < N \
            and c + dir_col[dir_idx] >= 0 and c + dir_col[dir_idx] < N \
            and not visited[r + dir_row[dir_idx]][c + dir_col[dir_idx]]:
            if area[r][c] > area[r + dir_row[dir_idx]][c + dir_col[dir_idx]]:
                # 등산로 가능
                dfs(r + dir_row[dir_idx], c + dir_col[dir_idx], visited, depth, fixed)
            elif not fixed:
                # 높이가 낮아서 불가하다면
                # 1 ~ K 만큼 공사하여 확인해보기
                for tmp_depth in range(1, K + 1):
                    area[r + dir_row[dir_idx]][c + dir_col[dir_idx]] -= tmp_depth
                    fixed = True
                    if area[r + dir_row[dir_idx]][c + dir_col[dir_idx]] < area[r][c]:
                        dfs(r + dir_row[dir_idx], c + dir_col[dir_idx], visited, depth, fixed)
                    else:
                        # 조건에 해당하지 않을 경우 max_depth와 비교 후 업데이트. 
                        # 해당 경로의 가장 마지막 노드임.
                        if depth > max_depth:
                            max_depth = depth
                    area[r + dir_row[dir_idx]][c + dir_col[dir_idx]] += tmp_depth
                    fixed = False
            else:
                # 조건에 해당하지 않을 경우 max_depth와 비교 후 업데이트. 
                # 해당 경로의 가장 마지막 노드임.
                if depth > max_depth:
                    max_depth = depth

    visited[r][c] = False
    depth -= 1

T = int(input())
for test_case in range(1, T + 1):
    # N area size, K 공사 가능 깊이
    N, K = map(int, input().split())
    area = []
    max_ = 0
    max_depth = 0
    h_queue = []
    for row in range(N):
        area.append([int(x) for x in input().split()])
        curr_max = max(area[-1])
        if max_ < curr_max:
            max_ = curr_max
            h_queue.clear()
            prev = 0
            for _ in range(area[row].count(max_)):
                h_queue.append((row, area[row].index(max_, prev)))
                prev = area[row].index(max_, prev) + 1
        elif max_ == curr_max:
            prev = 0
            for _ in range(area[row].count(max_)):
                h_queue.append((row, area[row].index(max_, prev)))
                prev = area[row].index(max_, prev) + 1

    while len(h_queue):
        row, col = h_queue.pop()
        visited = [copy.deepcopy([False] * N) for _ in range(N)]
        dfs(row, col, visited, 0, False)

    print(f'#{test_case} {max_depth}')
