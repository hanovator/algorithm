import sys
import numpy as np
from collections import deque

sys.stdin = open("in1.txt", "r")

# 12시, 3시 6시 9시 방향 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())  # N*N 격자판
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
print(np.array(a))

sum = 0
Q = deque()
ch[n // 2][n // 2] = 1  # 시작점 방문했다는 체크
sum += a[n // 2][n // 2]  # 가운데 시작점 값 더하기
Q.append((n // 2, n // 2))  # 가운데 시작점 BFS로 돌리기 위해 Q에 넣기
L = 0  # level

while True:
    if L == n // 2:
        break
    size = len(Q)
    print('Q -- ', Q)
    print('len(Q) -- ', len(Q))
    for i in range(size):
        tmp = Q.popleft()  # (행, 열)
        print('tmp -- ', tmp)
        print()
        for j in range(4):  # 4개의 가지를 친다.
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]  # 합을 구해준다.
                ch[x][y] = 1  # 해당값을 왔었다고 체크해 준다.
                Q.append((x, y))
    L += 1
print(sum)

