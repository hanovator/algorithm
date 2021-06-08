import sys
import numpy as np
from collections import deque

sys.stdin = open("in1.txt", "r")

# 상하좌우 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())  # m: 가로칸의 수, n: 세로칸의 수
board = np.array([list(map(int, input().split())) for _ in range(m)])
Q = deque()
dis = [[0] * n for _ in range(m)]
print(board)

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:  # 익은토마토 좌표(시작지점)
            Q.append((i, j))
print(Q)

while Q:  # 익은토마토를 시작으로 BFS
    x, y = Q.popleft()
    for i in range(4):  # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:  # 안익은 토마토일경우
            board[nx][ny] = 1  # 해당 토마토를 익은걸로 표시(재탐색 방지)
            dis[nx][ny] = dis[x][y] + 1  # 현재보다 뻗어진곳에 +1일을 더한다.
            Q.append((nx, ny))  # BFS로 뻗어진곳을 탐색하도록 que에 넣는다.

flag = 1
for i in range(m):  # 전부다 탐색했는지 확인
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

result = 0

if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:  # 가장큰 날짜 확인
                result = dis[i][j]
    print(result)
else:  # 익은 토마토가 없는경우 -1출력
    print(-1)
