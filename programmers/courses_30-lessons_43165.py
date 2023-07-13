# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버

# testcase 2개 시간초과
def bfs(numbers, target):
    result = 0
    q = []
    q.append((numbers[0], 0))
    q.append((numbers[0] * -1, 0))
  
    while len(q):
        curr, idx = q.pop(0)
            
        if idx == len(numbers) - 1 and curr == target:
            result += 1
            continue
            
        if idx < len(numbers) - 1:
            q.append((curr + numbers[idx+1], idx+1))
            q.append((curr - numbers[idx+1], idx+1))
    
    return result

# pass
def bfs2(numbers, target):
    result = 0
    q = [ [] for _ in range(20)]
    
    q[0].append(numbers[0])
    q[0].append(numbers[0] * -1)
    
    for idx, number in enumerate(numbers):
        if not idx: continue
        for prev in q[idx-1]:
            q[idx].append(prev+number)
            q[idx].append(prev-number)

    result = q[len(numbers)-1].count(target)
    return result


def solution(numbers, target):
    answer = 0
    #answer = bfs(numbers, target)
    answer = bfs2(numbers, target)
    return answer
