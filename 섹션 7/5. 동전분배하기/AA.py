import sys

sys.stdin = open("in1.txt", 'r')


def DFS(L):
    global res
    if L == n:  # 동전을 전부 사용 했다면
        cha = max(money) - min(money)
        if cha < res:  # 최대-최소 값이 현재 결과보다 작다면
            tmp = set()
            for x in money:  # 세사람이 가진 동전의 합 값이 서로 달라야한다. (문제 조건)
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):  # 세사람 가지치기
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]  # 이전 L로 돌아갈때 마지막 L 코인값을 빼준다.


if __name__ == "__main__":
    n = int(input())  # 동전의 개수
    coin = []
    tmp = []
    money = [0] * 3  # A,B,C 세사람
    res = 2147000000  # 답(최대, 최소의 차)
    for _ in range(n):
        coin.append(int(input()))  # 동전의 금액들
    DFS(0)
    print(res)
