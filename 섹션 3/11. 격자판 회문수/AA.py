import sys

sys.stdin = open("in1.txt", "r")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):  # 7*7 격자판이기 때문에 4이상은 5개 회문이 나올 수 없다.
    for j in range(7):
        tmp = board[j][i:i + 5]

        # tmp --  [2, 4, 1, 5, 3]
        # tmp[::-1] --  [3, 5, 1, 4, 2]

        if tmp == tmp[::-1]:
            cnt += 1

        # 열은 slice 할 수 없다.
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:  # 같은열의 세로 끝과 끝이 맞는지 비교.
                break;
        else:  # for문이 정상적으로 끝난경우: 전부 같은것이므로 회문!
            cnt += 1

print(cnt)
