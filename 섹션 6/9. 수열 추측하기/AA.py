import sys

sys.stdin = open("in1.txt", "rt")


def DFS(L, sum):
    # level 즉 깊이를 정해주는곳.
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        # 가지의 개수를 정해주는곳.
        for i in range(1, n + 1):
            if ch[i] == 0:  # 중복이 없는 순열.
                ch[i] = 1  # 이미 사용한것은 1로 체크.
                p[L] = i  # 순열 즉 답을 넣는다.
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())  # n: 시작숫자, f: 마지막 합  4,16.
    p = [0] * n  # 순열들을 만들어나갈곳.
    b = [1] * n  # 이항계수 변수 초기화.
    ch = [0] * (n + 1)

    # 이항계수 초기화 ex) 1331
    for i in range(1, n):  # 맨처음과 마지막은 1이다.
        b[i] = b[i - 1] * (n - i) // i
    DFS(0, 0)






