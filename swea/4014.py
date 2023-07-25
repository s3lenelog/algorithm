# 4014. [모의 SW 역량테스트] 활주로 건설
# 예외사항을 잘 보자
#import sys
#sys.stdin = open("input.txt", "r")

def check(m):
    '''
    :param m: 지형 정보 (row or col), list로 전달.
    :return: 활주로 O - True, X - False
    '''

    global N, X
    checked = [False] * N

    #for idx in range(N - X + 1):
    for idx in range(1, N):
        prev = idx - 1
        if m[prev] == m[idx]:
            continue
        # prev != m[idx]
        # 2 이상 차이날 경우 활주로 불가
        if abs(m[prev] - m[idx]) > 1:
            return False

        # 두 값의 차가 1인 경우
        # 더 작은 쪽 (prev)
        # -> m[prev-(X-1)] ~ m[prev]
        # (0) 활주로를 세울 수 있는 너비인지. (인덱스 범위가 넘어가는지)
        # (1) 모두 같은 값인지
        # (2) 이미 경사로가 있는지
        if m[prev] < m[idx]:
            if prev - (X - 1) < 0:  # (0) 인덱스 범위가 넘어가는지
                return False
            if all([m[prev-(X-1)] == tmp for tmp in m[prev-(X-1):prev+1]]) \
                and not any(checked[prev-(X-1):prev+1]):  # (1)모두 같은 값 & (2) 경사로 없어야 함.
                # 경사로 설치
                for i in range(prev-(X-1),prev+1):
                    checked[i] = True
            else:
                return False
        # 더 작은 쪽 (idx)
        else:
            if idx + X > N:  # m[idx:idx+X] -> idx ~ idx+(X-1)
                return False
            if all([m[idx] == tmp for tmp in m[idx:idx+X]]) \
                and not any(checked[idx:idx+X]):
                for i in range(idx, idx+X):
                    checked[i] = True
            else:
                return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    # N:지형 map size, X:경사로 너비
    N, X = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append([int(x) for x in input().split()])

    count = 0
    # row 단위 확인
    for row in maps:
        if check(row):
            count += 1

    # col 단위 확인
    for col in range(N):
        if check([row[col] for row in maps]):
            count += 1

    print(f'#{test_case} {count}')
