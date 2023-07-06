# 특이한 자석
# dfs, recursion 이용

def rotate(start, d, arrow, new_arrow, visited):
    ''' 
    - rotate()가 호출되면 한번 자석을 회전시켰을 때 recursion에 의해 조건에 맞는 자석이 회전된 결과(new_arrow)가 반환됨.
    - 화살표를 이동하는(인덱스를 변경) 방식으로 구현함(리스트 아이템을 좌우로 움직할 수도 있음)
    '''
    global g, m
    visited[start] = True
    new_arrow[start] = (new_arrow[start] - d) % 8

    for i in range(4):  # 4 nodes
        if g[start][i] and start != i and not visited[i]:  # check each node
            if start < i and m[start][(arrow[start] + 2) % 8] != m[i][(arrow[i] - 2) % 8]: # right
                new_arrow = rotate(i, -d, arrow, new_arrow, visited)
                continue
            if start > i and m[start][(arrow[start] - 2) % 8] != m[i][(arrow[i] + 2) % 8]: # left
                new_arrow = rotate(i, -d, arrow, new_arrow, visited)
                continue
    #visited[start] = False
    return new_arrow


if __name__ == '__main__':
    g = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    T = int(input())
    
    for testcase in range(1, T + 1):
        K = int(input())

        m = []
        for _ in range(4):
            m.append([int(x) for x in input().split()])
        
        arrow = [0] * 4
        for _ in range(K):  # get rotation data
            node_number, direction = [int(num) for num in input().split()]
            node_number -= 1
            arrow = rotate(node_number, direction, arrow, arrow.copy(), [False] * 4)

        total = 0
        for node, arrow_idx in enumerate(arrow):
            total += 2 ** node if m[node][arrow_idx] else 0

        print(f'#{testcase} {total}')
