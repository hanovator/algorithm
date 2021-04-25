import sys

sys.stdin = open("in1.txt", "r")


def DFS(L):
    global cnt
    if L == m:  # m번 다 뽑았을경우
        for i in range(m):  # res에 담겨있는 값 출력
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):  # n개(구슬개수)의 가지를 친다.
            res[L] = i
            DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
