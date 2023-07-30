# 1940. 가랏! RC카!

T = int(input())
for test_case in range(1, T+1):
    speed = 0  # m/s
    distances = 0
    N = int(input())
    for _ in range(N):
        command = [int(x) for x in input().split()]
        speed += command[1] if command[0] == 1 else 0 if not command[0] else (-1 * command[1])
        if speed < 0: speed = 0
        distances += speed
    print(f'#{test_case} {distances}')
