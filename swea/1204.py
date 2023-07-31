# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기

from collections import defaultdict

T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    scores = [int(x) for x in input().split()]
    counts = defaultdict(list)
    for score in set(scores):
        counts[scores.count(score)].append(score)    
    print(f'#{test_case} {max(counts[max(counts.keys())])}')
