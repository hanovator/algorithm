import sys

sys.stdin = open("in1.txt", "r")


def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0

# 각 입력라인을 불러와 Line 배열에 넣는다.
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)  # 가장 긴 값을 찾는다.(rt값을 위하여.)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
