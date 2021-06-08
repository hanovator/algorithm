import sys
from collections import deque
import numpy as np

sys.stdin = open("in1.txt", "r")

# 대각선 포함 시계방향 8방향 탐색
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n = int(input())  # 격자판
board = np.array([list(map(int, input().split())) for _ in range(n)])
print(board)
cnt = 0  # 섬의 개수
Q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 육지일경우
            board[i][j] = 0  # 0으로 초기화
            Q.append((i, j))  # 해당값부터 BFS로 시작하기위에 deque에 넣어준다

            while Q:
                tmp = Q.popleft()
                for k in range(8):  # 해당 위치에서 8방향 탐색
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:  # 격자판안에 있고 값이 1이라면
                        board[x][y] = 0  # 육지를 0인 바다로 초기화
                        Q.append((x, y))  # BFS를 위해 deque에 넣는다.

            cnt += 1  # while문에서 연결된 1들은 아일랜드 하나로 보기때문에 여기서 cnt+1

print(cnt)
