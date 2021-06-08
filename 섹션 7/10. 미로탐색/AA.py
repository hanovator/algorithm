import sys
import numpy as np
from collections import deque

sys.stdin = open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:  # 도착점 도착
        cnt += 1
    else:
        for i in range(4):  # 북 동 남 서
            xx = x + dx[i]  # 앞으로 갈 x
            yy = y + dy[i]  # 앞으로 갈 y
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:  # 격자판 밖은 x, 0: 갈 수 있는길
                board[xx][yy] = 1  # 지나간곳은 1로표시
                DFS(xx, yy)
                board[xx][yy] = 0


## 미로탐색(DFS)랑 in1.txt 값이 다름!!
if __name__ == "__main__":
    board = np.array([list(map(int, input().split())) for _ in range(7)])
    print(board)
    cnt = 0  # 결과 가지수
    board[0][0] = 1  # 시작지점은 이미 들린거니 1로 변환
    DFS(0, 0)
    print(cnt)
