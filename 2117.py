# 2117. [모의 SW 역량테스트] 홈 방범 서비스
#import sys
#sys.stdin = open("input.txt", "r")
import copy

def check(locations):
    global N, M
    max_ = 0
    for size in range(1, N + 2):  # size별로. N이 짝수이고 모서리 부분이 모두 1인 경우를 확인하기 위해서 N+1 size까지 확인해야함.
        price = size * size + (size - 1) * (size - 1)  # size에 따라 비용 고정
        for r in range(N):
            for c in range(N):
                # 지점 별 서비스 가능 가구 수 count
                count = 0
                # 예) h_locations와 각 지점 비교
                # abs(h_locations[0] - curr.r) + abs(h_locations[1] - curr.c) < size 이면 포함됨.
                for location in locations:
                    if abs(location[0] - r) + abs(location[1] - c) < size:
                        count += 1
                if count * M < price:  # 비용이 더 많이 든다면 손해임.
                    continue
                elif max_ < count:  # 최대인 경우 확인 및 저장
                    max_ = count

    return max_


T = int(input())
for test_case in range(1, T + 1):
    # N city size, M price per house
    N, M = map(int, input().split())
  
    h_locations = []
    for row in range(N):
        for col, x in enumerate(input().split()):
            if int(x):
                h_locations.append((row, col))  # 방범 서비스 지점 - 집 거리 비교를 위해 저장

    print(f'#{test_case} {check(h_locations)}')
