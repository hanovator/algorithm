import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum, time):
    global res
    if time > m:
        return  # 14번 줄로 가자!
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])  # 문제를 푼다.
        DFS(L + 1, sum, time)  # 문제를 풀지 않는다.


# 부분집합
if __name__ == "__main__":
    n, m = map(int, input().split())  # n: 문제 개수, m: 제한시간.
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())  # a: 점수, b: 소요시간.
        pv.append(a)  # 점수 저장.
        pt.append(b)  # 시간 저장.
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
