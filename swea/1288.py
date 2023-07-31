# 1288. 새로운 불면증 치료법

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    t = 0
    checked = [False] * 10

    while True:
        t += 1  	# t 번째
        target = t * N

        for i in range(len(str(target))):
            # 예)
            # 123 % 10 // 1 = 3
            # 123 % 100 // 10 = 2
            # 123 % 1000 // 100 = 1
            checked[(target % (10**(i+1))) // (10**i)] = True

        if all(checked):
            print(f'#{test_case} {target}')
            break
