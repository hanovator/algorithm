import sys

sys.stdin = open("in1.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 이분검색의경우 오름차순이건 내림차순이건 정렬이 되어있어야한다.
# 오름차순
a.sort()

lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2  # 중간값.
    if a[mid] == m:  # 중간값이 찾는값?
        print(mid + 1)
        break

    # 중간값보다 더 작면?
    elif a[mid] > m:
        rt = mid - 1  # 중간에서 한칸 적은값으로 이동.
    # 중간값보다 더 크다면?
    else:
        lt = mid + 1  # 중간에서 한칸 많은값으로 이동.
