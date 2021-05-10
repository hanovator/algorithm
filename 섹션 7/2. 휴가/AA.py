import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum):
    global res
    if L == n + 1:  # 휴가날짜가 되었을때!
        if sum > res:
            res = sum
    else:
        if L + T[L] <= n + 1:
            DFS(L + T[L], sum + P[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())  # 일 할수있는 날짜.
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)  # 소요시간.
        P.append(b)  # 금액.
    res = -2147000000
    T.insert(0, 0)  # 맨 앞 index에 0을 넣어 밀어줌.
    P.insert(0, 0)
    DFS(1, 0)
    print(res)
