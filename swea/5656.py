# SWEA [모의 SW 역량테스트] 벽돌 깨기
# bfs 벽돌 제거
# 중복순열 구하는 함수 구현
# 구슬 쏜 후 벽돌 정리하는 함수 구현

import copy
import time
N, W, H = -1, -1, -1
result = 999
init_bricks = []


def clear_bricks(curr):
    global W, H

    for col in range(W):
        new_bricks = []
        for row in range(H):
            data = curr[row][col]
            if data:
                new_bricks.append(data)
            else:
                new_bricks.insert(0, data)

        for row in range(H):
            curr[row][col] = new_bricks[row]

    return curr


# bfs() 호출 시 curr를 init_bricks로 초기화
def bfs(shoot_list, curr):
    q = []
    for col in shoot_list:
        q = []
        for row in range(H):
            # 1.구슬 한 번 쏘기
            # bfs
            data = curr[row][col]
            if not data:
                continue
            q.append((row, col))
            while len(q):
                r, c = q.pop()

                # index check
                if r < 0 or c < 0 or r > H-1 or c > W-1:
                    continue

                data = curr[r][c]
                if not data:  # 0이면 이미 벽돌이 없으므로 continue
                    continue

                curr[r][c] = 0
                for i in range(data):
                    # 파괴 가능한 벽돌 인덱스를 큐에 추가
                    # up
                    if r - i >= 0:
                        q.append((r - i, c))
                    # down
                    if r + i < H:
                        q.append((r + i, c))
                    # left
                    if c - i >= 0:
                        q.append((r, c - i))
                    # right
                    if c + i < W:
                        q.append((r, c + i))
            break  # 한 번 쏜 후에 break하여 다음 shoot_list의 컬럼으로 쏘아야 함.

        # 2. 벽돌 정리
        curr = clear_bricks(curr)
        #print_bricks(curr)

    count = 0
    # 해당 shoot_list로 쏠 경우 결과 값을 저장하고 반환.
    # 0 개수를 구하고 W*H에서 빼서 구함.
    for row in curr:
        count += row.count(0)

    return W * H - count


def permutation(shoot_list, depth):
    global W, N, init_bricks, result

    if depth > N - 1:
        # 생성된 shoot_list 이용해 bfs() 호출
        # bfs() 호출 전에 입력받은 초기 벽돌 상태로 세팅
        curr = copy.deepcopy(init_bricks)
        res = bfs(shoot_list, curr)
        if result > res:
            result = res
        return

    for i in range(W):
        # 구슬 번호 세팅
        shoot_list.append(i)
        permutation(shoot_list, depth + 1)  # 다음 구슬 번호
        # 구슬 번호 제거
        shoot_list.pop()

def print_bricks(b):
    for i in b:
        print(i)

def init():
    global W, H, init_bricks, N, result
    T = int(input())

    for test_case in range(1, T + 1):
        #start = time.time()  # 실행 시간 계산

        # N 구슬 쏘기 횟수, W cols, H rows
        N, W, H = map(int, input().split())
        init_bricks.clear()
        result = 999
        for _ in range(H):
            init_bricks.append(list(map(int, input().split())))

        permutation([], 0)
        print(f'#{test_case} {result}')
        # print(f'#{test_case} {result} : {time.time()-start:.4f} sec')  # 실행 시간 계산

init()
