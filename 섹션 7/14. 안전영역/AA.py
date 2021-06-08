import sys
import numpy as np

sys.stdin = open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)


def DFS(x, y, h):
    ch[x][y] = 1 # 이미 간곳으로 체크
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())  # n*n 행렬
    cnt = 0
    res = 0  # 최종답
    board = np.array([list(map(int, input().split())) for _ in range(n)])
    print(board)

    for h in range(100):  # 높이를 정한다.
        ch = np.array([[0] * n for _ in range(n)])  # n*n ch 행렬
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:  # 일정 높이보다 높을경우
                    cnt += 1 # 인근지역에서 연결되는 구조지역
                    DFS(i, j, h)
        res = max(res, cnt)  # 장마 높이가 바뀌면서 가장 큰 구역수를 결과값으로 반환

        if cnt == 0:  # 장마 높이 h보다 높은값이 없는경우 나온다.
            break
    print(res)
