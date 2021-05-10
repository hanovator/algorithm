import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum):
    global res
    print('l -- ', L)
    if L == n:  # 추의 개수를 전부 사용시.
        if 0 < sum <= s:  # 추의 총 무게 s를 넘기면 안된다.
            res.add(sum)
    else:
        DFS(L + 1, sum + G[L])  # 추를 오른쪽에
        DFS(L + 1, sum - G[L])  # 추를 왼쪽에
        DFS(L + 1, sum)  # 해당추만 사용


if __name__ == "__main__":
    n = int(input())  # 추 개수
    G = list(map(int, input().split()))  # 각추들의 무게
    s = sum(G)  # 추들의 총 무게
    res = set()  # 중복 제거
    DFS(0, 0)
    print(s - len(res))




