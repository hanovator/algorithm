import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())  # n:입력숫자 개수, k: 조합에 사용할 숫자 개수.
    a = list(map(int, input().split()))  # 입력 숫자들.
    m = int(input())  # 조합 숫자들의 합의 배수가될 숫자.
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)