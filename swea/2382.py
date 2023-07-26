# SWEA [모의 역량 테스트] 미생물 격리
#import sys
#sys.stdin = open("input.txt", "r")
import copy

# (상: 1, 하: 2, 좌: 3, 우: 4)
d_row = [0, -1, 1, 0, 0]
d_col = [0, 0, 0, -1, 1]


def check(i):
    '''
    :param i: 미생물 군집 정보 (list)
    :return: 남은 미생물 수 (int)
    '''
    global M, K, N
    t = 0

    while True:

        for idx in range(len(i)):
            if not i[idx][2]:  # 미생물 수가 0이면 사라진 군집
                continue
            # 1. 이동 (d_row, d_col을 이용)
            i[idx][0] += d_row[i[idx][3]]
            i[idx][1] += d_col[i[idx][3]]

            # 2. 약품처리한 위치 확인
            if i[idx][0] == 0 or i[idx][0] == N-1 \
                    or i[idx][1] == 0 or i[idx][1] == N-1:
                # 2-1. [O] 미생물 수 절반으로 감소
                # 2-1-1. 미생물 수가 0이면 미생물 군집 i에서 제거(미생물 수 0)
                # 2-1-2. 미생물 수가 남아있으면 방향을 반대로 변경
                if int(i[idx][2] / 2) < 1:
                    i[idx][2] = 0
                else:
                    i[idx][2] = int(i[idx][2] / 2)
                    if i[idx][3] % 2:
                        i[idx][3] += 1  # 1, 3이면 1 증가
                    else:
                        i[idx][3] -= 1  # 2, 4이면 1 감소

        ################################
        # 3. 공통 위치?
        # 3-1. 가장 많은 미생물 수 군집 확인
        # 3-2. 최다 군집에 미생물 수 추가 후 나머지 군집 삭제(방향 0)
        sorted_i = sorted(i, key=lambda x: (x[0], x[1], x[2]))
        idx = 0
        for idx in range(len(sorted_i) - 1):
            if not sorted_i[idx][2]:  # 사라진 군집은 비교하지 않음.
                continue
            if sorted_i[idx][0] == sorted_i[idx+1][0] \
                    and sorted_i[idx][1] == sorted_i[idx+1][1] and sorted_i[idx][3]:
                # 미생물 수에 따라 오름차순 정렬했으니까 바로 위치 같은 다음 군집에 미생물 수 누적
                sorted_i[idx+1][2] += sorted_i[idx][2]
                sorted_i[idx][2] = 0  # 미생물 수를 0으로 세팅하여 적은 군집은 제거

        ################################
        i = sorted_i
        # 4. 시간 증가
        # 4-1. M시간 후에는 모든 군집의 미생물 수 합을 반환.
        # - 미생물 수가 0이면 사라진 군집
        t += 1
        if t == M:
            return sum([x[2] for x in i if x[2]])


T = int(input())
for test_case in range(1, T + 1):
    # N area size, M total time, K 군집 수
    N, M, K = map(int, input().split())
    infos = []
    for _ in range(K):
        infos.append(list(map(int, input().split())))
        #infos.append([int(x) for x in input().split()])

    print(f'#{test_case} {check(infos)}')
