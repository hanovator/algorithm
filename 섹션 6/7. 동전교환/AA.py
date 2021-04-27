import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum):
    global res
    if L >= res:  # res가 최소의 값이 되야함으로 더 큰값이 있다면 return!
        return
    if sum > m:  # 만들어야할 동전(m) 보다 현재까지 더한 거스름돈의 크기(sum)가 더 크면 return
        return
    if sum == m:  # 현재까지 더한 거스름돈의 크기(sum)가 거스름돈(m)과 같다면
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, sum + a[i])


if __name__ == "__main__":
    n = int(input())  # 동전의 개수 3
    a = list(map(int, input().split()))  # 동전의 종류 1 2 5
    m = int(input())  # 만들어야할 동전 15
    res = 2147000000  # 최소값을 넣어야 한다. (가장 최소의 거스름돈 개수를 구해야하기 때문에)
    a.sort(reverse=True)  # 큰값을 먼저 넣어본다.
    DFS(0, 0)
    print(res)
