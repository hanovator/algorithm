import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, s):
    global cnt
    if L == m:  # level이 조합의 뽑아야할 숫자와 같다면
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)  # level증가, 가지수 1부터가 아닌 i+1부터로 (조합이라서..)


n, m = map(int, input().split())
res = [0] * (n + 1)
cnt = 0
DFS(0, 1) 
print(cnt)