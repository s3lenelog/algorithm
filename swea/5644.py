#sys.stdin = open("input.txt", "r")

import copy
def print_position(map):
    for bc_ in map:
        print(bc_)
dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

T = int(input())

for test_case in range(1, T + 1):

    # M 이동시간, A BC수
    M, A = map(int, input().split())
    user_A_pos = [(1, 1)]
    user_B_pos = [(10, 10)]
    for idx, curr_dir in enumerate(input().split()):
        curr_dir = int(curr_dir)
        user_A_pos.append((user_A_pos[idx][0] + dir[curr_dir][0], user_A_pos[idx][1] + dir[curr_dir][1]))
    for idx, curr_dir in enumerate(input().split()):
        curr_dir = int(curr_dir)
        user_B_pos.append((user_B_pos[idx][0] + dir[curr_dir][0], user_B_pos[idx][1] + dir[curr_dir][1]))

    bc_infos = []
    for bc in range(A):
        bc_info = [int(x) for x in input().split()]
        bc_infos.append(copy.deepcopy(bc_info))

    # 가장 큰 합의 값을 결과로 출력 -> 충전 성능(P)를 기준으로 내림차순 정렬
    bc_infos.sort(key=lambda x:x[3], reverse=True)
    #print(bc_infos)

    # 사용자 A,B의 location 마다 충전 가능한 BC의 인덱스 저장(bc_infos index)
    a_bc_list = []
    b_bc_list = []
    # each position -> how much charged
    for a_pos, b_pos in zip(user_A_pos, user_B_pos):
        a_bc_list.append([])  # 각 지점마다 충전가능한 BC 인덱스 목록을 리스트로 저장
        b_bc_list.append([])
        for idx, bc_info in enumerate(bc_infos):
            if not bc_info[2] < abs(a_pos[0] - bc_info[1]) + abs(a_pos[1] - bc_info[0]):  # 해당 BC에 사용자가 충전 가능한지 확인
                a_bc_list[-1].append(idx)
            if not bc_info[2] < abs(b_pos[0] - bc_info[1]) + abs(b_pos[1] - bc_info[0]):
                b_bc_list[-1].append(idx)


    total = 0
    for a_bc, b_bc in zip(a_bc_list, b_bc_list):
        if not len(a_bc):  # a = 0
            # a == 0 & b == 0 인 경우에는 아무 동작도 하지 않아도 됨.
            if len(b_bc):  # a == 0, b != 0
                total += bc_infos[b_bc[0]][3]
            continue

        else:  # a != 0
            if not len(b_bc): # a != 0 & b == 0
                total += bc_infos[a_bc[0]][3]
                continue

        # a != 0 & b != 0
        # 겹칠 때 -> 내림차순으로 정렬했으므로 크게 상관없음.
        if a_bc[0] == b_bc[0]:
            # 1. 둘 다 원소가 하나라서 무조건 겹칠 때,
            if len(a_bc) == 1 and len(b_bc) == 1:
                total += bc_infos[a_bc[0]][3]  # 절반이므로 둘 합친 값으로 생각하고 넣음.
            # 2. 둘 중 한 경우만 1일 때
            # 2-1. a만
            elif len(a_bc) == 1:
                total += bc_infos[a_bc[0]][3]
                total += bc_infos[b_bc[1]][3]  # b가 0, 1 모두 아니므로 최소 2이상임
            # 2-2. b만
            elif len(b_bc) == 1:
                total += bc_infos[a_bc[1]][3]  # a가 0, 1 모두 아니므로 최소 2이상임
                total += bc_infos[b_bc[0]][3]  
            # 3. 둘다 2개 이상일 때
            # 각 BC의 performance(P)를 더했을 때 더 P가 높은 경우를 더해줌
            elif bc_infos[a_bc[0]][3] + bc_infos[b_bc[1]][3] > bc_infos[a_bc[1]][3] + bc_infos[b_bc[0]][3]:  
                #print(f'{a_bc[0]} vs {b_bc[0]}')
                total += bc_infos[a_bc[0]][3]
                total += bc_infos[b_bc[1]][3]
            else:
                total += bc_infos[a_bc[1]][3]
                total += bc_infos[b_bc[0]][3]

        # 겹치지 않을 때, (둘다 가장 큰 첫 번째 P 더해줌)
        else:
            total += bc_infos[a_bc[0]][3]
            total += bc_infos[b_bc[0]][3]

    print(f'#{test_case} {total}')
