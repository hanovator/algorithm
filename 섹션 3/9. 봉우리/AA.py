import sys

sys.stdin = open("in1.txt", 'r')

# 상하좌우 검색.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())  # n * n의 격자판을 만들 n.
a = [list(map(int, input().split())) for _ in range(n)]

# 아래 위에 0행렬 추가.
a.insert(0, [0] * n)  # 0번행에 0행렬 추가.
a.append([0] * n)  # 마지막행에 0행렬 추가.

# 왼쪽 오른쪽에 0행렬 추가.
for x in a:
    x.insert(0, 0)  # 0번행에 0 추가.
    x.append(0)  # 마지막행에 0 추가.

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):  # 상하좌우 탐색.
            cnt += 1
print(cnt)
