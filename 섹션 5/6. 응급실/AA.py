import sys
from collections import deque

sys.stdin = open("in2.txt", "r")

# n: 환자의 수. 5
# m: 진료받기위한 환자. 2
n, m = map(int, input().split())
q_list = list(map(int, input().split()))  # [60, 50, 70, 80, 90]
print('q_list -- ', q_list)

Q = [(pos, val) for pos, val in enumerate(q_list)]  # [(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]
print('Q -- ', Q)

Q = deque(Q)
cnt = 0

while True:  # break가 나올때까지 계속돈다.
    cur = Q.popleft()  # 순서가 가장 먼저인 환자.
    if any(cur[1] < x[1] for x in Q):  # 현재보다 위험도가 높은환자가 한명이라도 있다면 현재 환자를 제일 뒤로 보낸다.
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:  #
            print(cnt)
            break
