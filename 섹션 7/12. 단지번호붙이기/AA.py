import sys
import numpy as np

sys.stdin = open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0  # 거쳤던곳은 0으로

    for i in range(4):
        xx = x + dx[i]  # 상우하좌 ex) 상(x-1 행)
        yy = y + dy[i]  # 상우하좌 ex) 상(y+0 열)

        # n*n행렬 안에 있고, 행렬값이 1인경우 DFS
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = np.array([list(map(int, input())) for _ in range(n)])
    print(board)
    res = []

    # 행열탐색
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 집이 발견되면 DFS 탐색시작!
                cnt = 0  # DFS를 돌기전 cnt 초기화화
                DFS(i, j)
                res.append(cnt)

    print(len(res))
    res.sort()
    for x in res:
        print(x)
