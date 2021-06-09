import sys
import numpy as np

sys.stdin = open("in1.txt", "r")


def DFS(x, y):
    ch[x][y] = 1
    if x == 0:  # 처음으로 온 경우
        print(y)  # 해당 열을 출력
    else:
        if y - 1 >= 0 and board[x][y - 1] == 1 and ch[x][y - 1] == 0:  # 좌측 살핌
            DFS(x, y - 1)  # 좌로감
        elif y + 1 < 10 and board[x][y + 1] == 1 and ch[x][y + 1] == 0:  # 우측 살핌
            DFS(x, y + 1)  # 우로감
        else:
            DFS(x - 1, y)  # 위로 올라감


board = np.array([list(map(int, input().split())) for _ in range(10)])
ch = np.array([[0] * 10 for _ in range(10)])

for y in range(10):
    if board[9][y] == 2:  # 마지막 행의 값이 2인경우.
        DFS(9, y)  # 거꾸로 사다리를 탄다. (9,5)
