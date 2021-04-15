import sys
from collections import deque

sys.stdin = open("in1.txt", "r")
need = input()  # 필수과목.
print('need -- ', need)
n = int(input())  # 수강신청한 계획들.
print('n -- ', n)
print()

# 수강신청한 계획들만큼 for문.
for i in range(n):
    plan = input()  # 수강신청 계획.
    dq = deque(need)  # 필수과목을 큐에 넣는다.
    print('plan -- ', plan)
    print('dq -- ', dq)

    for x in plan:
        if x in dq:  # 수강신청 계획과목중에 필수과목이 있다면.
            # dq.popleft()로 비교하면서 자동으로 큐에서 제일 왼쪽과목이 빠져나옴.            if x != dq.popleft():  # 계획과목중 필수과목이라면 큐에서 순서 체크.
            print("#%d NO" % (i + 1))
            break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))

    print()
