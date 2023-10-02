# 프로그래머스 - 코딩테스트 연습 (DP)
# N으로 표현
def solution(N, number):
    answer = 0
    if N == number:
        return 1

    dp = [{N}]
    for depth in range(2, 9):
        dp.append(set())
        if int(str(N) * depth) == number:
            return depth

        dp[depth - 1].add(int(str(N) * depth))
        for dp_ in range(1, depth // 2 + 1):
            prev1 = dp[dp_ - 1]
            prev2 = dp[depth - dp_ - 1]
            for p1 in prev1:
                for p2 in prev2:
                    dp[depth - 1].add(p1 + p2)  # + 
                    dp[depth - 1].add(p1 - p2)  # -
                    dp[depth - 1].add(p2 - p1)  # - 반대로
                    dp[depth - 1].add(p1 * p2)  # *
                    if p2:
                        dp[depth - 1].add(p1 // p2)  # // 
                    if p1:
                        dp[depth - 1].add(p2 // p1)  # // 반대로

        if number in dp[depth-1]:
            return depth

    answer = -1
    return answer    

if __name__ == '__main__':
    print(solution(5, 12), 4)
    print(solution(5, 31168), -1)
    print(solution(4, 31), 5)
    print(solution(8, 53), 5)
    print(solution(1, 1121), 7)
