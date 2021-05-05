import sys
import numpy as np

sys.stdin = open("in1.txt", "r")


def DFS(v):  # v: node 번호.
    global cnt, path
    if v == n:  # 종착지점 도착.
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):  # 가지를 뻗는다.
            if g[v][i] == 1 and ch[i] == 0:  # 경로가 있고, 중복방문이 아닌경우.
                ch[i] = 1
                path.append(i)  # 정답 path에 추가.
                print('v1 -- ', v)
                print('i1 -- ', i)
                DFS(i)
                print('v2 -- ', v)
                print('i2 -- ', i)
                path.pop()  # 이전 depth로 올라가기전에 path에서 제외.
                ch[i] = 0  # 이전 depth로 올라가기전에 check를 풀어준다.


if __name__ == "__main__":
    n, m = map(int, input().split())  # n: node 번호, m: 전체 간선정보의 개수.
    g = [[0] * (n + 1) for _ in range(n + 1)]  # node에 맞는 정방향 matrix를 만든다.
    ch = [0] * (n + 1)  # 이미 거친 node를 체크해 준다.
    print(np.array(g))
    print('ch -- ', ch)
    print()

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1

    print(np.array(g))
    print()

    cnt = 0
    ch[1] = 1  # 1번 node부터 시작하기때문에 1번 node check!
    path = list()
    path.append(1)
    DFS(1)
    print(cnt)