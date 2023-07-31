# 5653. [모의 SW 역량테스트] 줄기세포배양

import time
import copy 

dir_row = [-1, 1, 0, 0]
dir_col = [0, 0, -1, 1]

# 무제한으로 나와 있었지만, 
# row, col 저장해서 확인할 경우 시간 초과가 나서
# 디버깅하면서 1000 정도로 잡고 함.
visited = [copy.deepcopy([False] * 1000) for _ in range(1000)]

def check(cells):
    global N, M, K, visited
    t = 0
    while True:
        # 1. cells 정렬
        # 생명력 순으로 세포 정렬
        # 생명력 높은 순으로 있기 때문에 new_cells에도 생명력 높은 순으로 번식함.
        # -> 생명력을 비교하지 않아도 됨.
        cells.sort(key=lambda x: x[2], reverse=True)

        new_cells = []
        for cell in cells:
            # 생명령을 하나씩 감소함. 0인 경우 active 처음 1시간이므로 번식을 함.
            if 0 == cell[3]:  
                for dir_idx in range(4):  # 상하좌우
                    # python에서는 음수 인덱스로 되어도 동일한 결과 나옴.
                    # 번식되지 않은 셀이면 new_cells에 추가 & visited 세팅
                    if not visited[cell[0] + dir_row[dir_idx]][cell[1] + dir_col[dir_idx]]:  
                    # if not visited[(cell[0] + dir_row[dir_idx]) % 1000][(cell[1] + dir_col[dir_idx]) % 1000]:
                        new_cells.append([cell[0] + dir_row[dir_idx],
                                          cell[1] + dir_col[dir_idx],
                                          cell[2],
                                          cell[2]])
                        visited[cell[0] + dir_row[dir_idx]][cell[1] + dir_col[dir_idx]] = True
                        # visited[(cell[0] + dir_row[dir_idx]) % 1000][(cell[1] + dir_col[dir_idx]) % 1000] = True
                    
            #  
            # if (-1 * cell[2]) == cell[3]:
            #     continue

            cell[3] -= 1

        cells += new_cells

        t += 1
        if t == K:
            break
    
    result = 0
    for cell in cells:
        # if not (-1) * cell[2] == cell[3]:
        # 현재 남은 생명력이 세포 생명력 * (-1) 보다 작거나 같으면 죽은 세포임.
        if not (-1) * cell[2] >= cell[3]:
            result += 1

        # visited 초기화
        visited[cell[0]][cell[1]] = False
            
    return result


T = int(input())
for test_case in range(1, T + 1):
    # N row size, M col size, K 배양시간
    start = time.time()
    N, M, K = map(int, input().split())
    init_cells = []

    for row in range(N):
        for col, k in enumerate(input().split()):   # k 각 세포의 생명력
            k = int(k)
            if k:
                init_cells.append([row, col, k, k])
                visited[row][col] = True

    print(f'#{test_case} {check(init_cells)}')
    # print(f'#{test_case} {check(init_cells)} : {time.time()-start:.4f} sec')
