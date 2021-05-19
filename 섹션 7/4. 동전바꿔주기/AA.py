import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum):
    global cnt
    if sum > m:  # 합친 금액이 기준금액보다 크다면
        return
    if L == n:  # 모든 동전을 다 사용했다면
        if sum == m:
            cnt += 1
    else:
        # 해당 동전의 개수만큼 가지를 친다.
        for i in range(cn[L] + 1):  # L: 동전, cn[L]: 해당 동전의 개수
            DFS(L + 1, sum + (cv[L] * i))  # cv[L]: 해당 동정의 금액


if __name__ == "__main__":
    m = int(input())  # 지폐금액
    n = int(input())  # 동전의 가지수
    cv = list()
    cn = list()
    for i in range(n):
        a, b = map(int, input().split())  # a: 동전의 금액, b: 개수
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)
