import copy
import time
#sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # start = time.time()

    # N 숫자 개수, K 몇 번째로 큰 숫자인지
    N, K = map(int, input().split())
    side = int(N / 4)
    _in = input()
    numbers = [copy.deepcopy(_in[idx:idx+side]) for idx, x in enumerate(_in) if not idx % side]

    # 회전 : side - 1 만큼 회전 후 저장
    # -> 이미 위에서 초기 상태 데이터는 저장했으니까
    for _ in range(side - 1):
        # rotate
        _in = _in[1:] + _in[0]

        # numbers 저장 & 중복 제거
        for idx, x in enumerate(_in):
            if not idx % side:
                numbers.append(copy.deepcopy(_in[idx:idx+side]))

    # 중복제거 & 내림차순 정렬
    numbers = list(set(numbers))
    numbers.sort(reverse=True)

    # 이진수 -> 십진수 변환하여 출력
    print(f'#{test_case} {int(numbers[K-1], 16)}')
	  #print(f'#{test_case} {int(numbers[K-1], 16)}  : {time.time()-start:.4f} sec')
  
