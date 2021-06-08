import sys
import numpy as np
from collections import deque

sys.stdin = open("in1.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = np.array([list(map(int, input().split())) for _ in range(7)])
dis = np.array([[0] * 7 for _ in range(7)])  # 빈 7*7 matrix
Q = deque()
Q.append((0, 0))
board[0][0] = 1  # 시작점은 이미 갔으므로 1로 초기화

print(board)
print()
print(dis)
print()

while Q:
    print(Q)
    print()
    tmp = Q.popleft()  # BFS
    for i in range(4):  # 가지를 4개 친다.
        # 동서남북 시계방향으로 확인
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]

        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:  # 해당 검색블록이 도로인경우
            board[x][y] = 1  # 이미 갔으므로 되돌아가지 못하도록 블록 1을 쌓아줌
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1  # 부모가지의 값에 1을 더해준다
            Q.append((x, y))  # 가지가 쳐진곳은 계속 가지가 쳐지도록 deque에 넣어준다
print(dis)
if dis[6][6] == 0:  # 도착점에 도착 할 수 없는경우
    print(-1)
else:
    print(dis[6][6])
