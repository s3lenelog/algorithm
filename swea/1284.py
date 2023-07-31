# 1284. 수도 요금 경쟁
T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # A 요금 : P * W 
    # B 요금 : Q + max(W-R, 0) * S 
    result = P * W if (P * W) < (Q + max(W-R, 0) * S) else (Q + max(W-R, 0) * S)
    print(f'#{test_case} {result}')
  
