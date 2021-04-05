import sys

sys.stdin = open("in1.txt", "r")


# 말의 개수를 counting한다.
def Count(mid):

    cnt = 1
    ep = Line[0]  # 가장 앞의 말.

    for i in range(1, n):  # 마구간의 개수만큼 for문을 돌린다.
        if Line[i] - ep >= mid:  # 두 말의 거리가 지정한 값보다 크면 말의 개수 cnt를 올려준다.
            cnt += 1  # 말의 개수
            ep = Line[i]  # 가장 앞의 말을 바꿔준다.

    return cnt


# n: 마구간의 수, c: 말의 개수
n, c = map(int, input().split())
Line = []  # 말들이 마구간에 들어가있는 순서.

for _ in range(n):
    tmp = int(input())
    Line.append(tmp)

Line.sort()  # 이분검색을 위해 먼저 정렬을 해 준다.
lt = 1
rt = Line[n - 1]  # 마지막 말의 위치.

# 이분검색 시작
while lt <= rt:

    mid = (lt + rt) // 2

    if Count(mid) >= c:  # counting된 개수가 말의개수(c)보다 크거나 같으면 통과!
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
