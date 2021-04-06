import sys

sys.stdin = open("in2.txt", "r")

L = int(input())  # 창고의 길이.
a = list(map(int, input().split()))  # 각 창고의 높이.
m = int(input())  # 높이조정 횟수.
a.sort()
print('a -- ', a)

# 높이를 m만큼 조정한다.
for _ in range(m):
    print('a[0] -- ', a[0])
    print('a[L - 1] -- ', a[L - 1])
    a[0] += 1
    a[L - 1] -= 1
    a.sort()

print(a[L - 1] - a[0])
