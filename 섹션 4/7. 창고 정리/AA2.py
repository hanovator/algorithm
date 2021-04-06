import sys

sys.stdin = open("in2.txt", "r")

L = int(input())  # 창고의 길이.
arr = list(map(int, input().split()))  # 각 창고의 높이.
m = int(input())  # 높이조정 횟수.
cnt = [0] * 101

maxH = float('-inf')
minH = float('inf')

for x in arr:
    cnt[x] += 1
    if x > maxH: maxH = x
    if x < minH: minH = x

print('arr -- ', arr)
print('maxH -- ', maxH)
print('minH -- ', minH)
print('cnt -- ', cnt)

# 제일 컸던게 어차피 -1 줄어도 계속 제일 클 가능성이 높다..
for _ in range(m):

    # 가장 큰 값의 cnt가 1일경우.
    if cnt[maxH] == 1:
        cnt[maxH] -= 1  # 가장 큰 cnt에 1을 빼서 0으로 만들어준다.
        maxH -= 1  # 하나 줄여준다.

        # 91이 두번 나오는 이유는 92가 최대였는데 이를 1 줄여주면 원래있는 91이 나타나서이다..
        print('maxH -- 22 -- ', maxH)
        cnt[maxH] += 1  # 하나 줄여준 cnt에 1을 더해준다.  ex) 87이 가장 컸으므로 86
    else:
        cnt[maxH] -= 1
        cnt[maxH - 1] += 1
        print('maxH -- 33333 -- ', maxH)

    # 가장 작은 값의 cnt가 1일경우.
    if cnt[minH] == 1:
        cnt[minH] -= 1
        minH += 1
        cnt[minH] += 1
        # print('minH -- 22 -- ', minH)
    else:
        cnt[minH] -= 1
        cnt[minH + 1] += 1
        # print('minH -- 33333 -- ', minH)

    print('=======================')

# print('aaa maxH -- ', maxH)
# print('aaa minH -- ', minH)
print(maxH - minH)
