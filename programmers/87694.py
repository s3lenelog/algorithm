# 프로그래머스 코딩테스트 연습 - 아이템 줍기
import copy
from collections import deque

d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # up down right left

def bfs(outer, q, itemX, itemY):
    visited = [copy.deepcopy([False] * 102) for _ in range(102)]
  
    while len(q):
        depth, cx, cy = q.pop()
        if cx == itemX and cy == itemY:
            return depth

        visited[cx][cy] = True

        # up d[0]
        if (cx + d[0][0], cy + d[0][1]) in outer and not visited[cx + d[0][0]][cy + d[0][1]]:
            q.appendleft((depth + 1, cx + d[0][0], cy + d[0][1]))
            # visited[cx + d[0][0]][cy + d[0][1]] = True

        # down d[1]
        if (cx + d[1][0], cy + d[1][1]) in outer and not visited[cx + d[1][0]][cy + d[1][1]]:
            q.appendleft((depth + 1, cx + d[1][0], cy + d[1][1]))
            # visited[cx + d[1][0]][cy + d[1][1]] = True

        # right d[2]
        if (cx + d[2][0], cy + d[2][1]) in outer and not visited[cx + d[2][0]][cy + d[2][1]]:
            q.appendleft((depth + 1, cx + d[2][0], cy + d[2][1]))
            # visited[cx + d[2][0]][cy + d[2][1]] = True

        # left d[3]
        if (cx + d[3][0], cy + d[3][1]) in outer and not visited[cx + d[3][0]][cy + d[3][1]]:
            q.appendleft((depth + 1, cx + d[3][0], cy + d[3][1]))
            # visited[cx + d[3][0]][cy + d[3][1]] = True

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
  
    outer = set()
    inner = set()
    for x1, y1, x2, y2 in rectangle:
        outer.update({(x, y) for x in range(2 * x1, 2 * x2 + 1) for y in range(2 * y1, 2 * y2 + 1)})
        inner.update({(x, y) for x in range(2 * x1 + 1, 2 * x2) for y in range(2 * y1 + 1, 2 * y2)})
        outer -= inner

    q = deque()
    q.appendleft((0, 2 * characterX, 2 * characterY))
    answer = bfs(outer, q, 2 * itemX, 2 * itemY) // 2
    return answer

if __name__ == '__main__':
    print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8), 17)
    print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1), 11)
    print(solution([[1, 1, 5, 7]], 1, 1, 4, 7), 9)
    
