import sys

sys.stdin = open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x == ex and y == ey:  # 최대값이 있는곳으로 도착을 했다면
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]  # 상하좌우 x 탐색
            yy = y + dy[k]  # 상하좌우 y 탐색

            # 가려는 지점이 현재 지점보다 커야한다
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1  # 현재보다 큰곳을 찾은경우 1로 마킹
                DFS(xx, yy)  # go deeper place
                ch[xx][yy] = 0  # 해당 지역 0으로 초기화


if __name__ == "__main__":
    n = int(input())  # 격자판의 크기
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]  # 체크리스트
    max = -2147000000
    min = 2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))  # 격자를 한줄씩 읽는다.
        for j in range(n):
            if tmp[j] < min:  # 최소값 발견
                min = tmp[j]
                sx = i  # 최소값 x
                sy = j  # 최소값 y
            if tmp[j] > max:  # 최대값 발견
                max = tmp[j]
                ex = i  # 최대값 x
                ey = j  # 최대값 y
            board[i][j] = tmp[j]  # 등산로 격자판

    ch[sx][sy] = 1  # 첫 출발지점 체크!
    cnt = 0
    DFS(sx, sy)
    print(cnt)
