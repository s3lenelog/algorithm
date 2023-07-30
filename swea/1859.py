# 1859. 백만 장자 프로젝트

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = [int(x) for x in input().split()]
    result = 0
    prev = 0
    while True:
        if len(prices) < 2:
            print(f'#{test_case} {result}')
            break
        max_ = max(prices)
        max_idx = prices.index(max_)
        for price in prices[:max_idx+1]:
            result += max_ - price
        prices = prices[max_idx+1:]
