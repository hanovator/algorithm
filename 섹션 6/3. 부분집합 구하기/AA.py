import sys

sys.stdin = open("in1.txt", "r")


def DFS(v):
    if v == n + 1:  # n까지는 출력이 되야 함으로 n+1로 계산.
        for i in range(1, n + 1):
            if ch[i] == 1:  # 사용하는 경우 출력.
                print(i, end=' ')
        print()
    else:
        ch[v] = 1  # 사용한다.
        DFS(v + 1)
        ch[v] = 0  # 사용하지 않는다.
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)  # 사용 할지 않할지 체크하는 변수.
    DFS(1)
