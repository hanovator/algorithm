import sys
from collections import deque

sys.stdin = open("in1.txt", "r")

n, limit = map(int, input().split())
p = list(map(int, input().split()))  # 각 승객의 몸무게.
p.sort()  # 몸무게를 오름차순으로 정렬.
p = deque(p)  # 양쪽으로 넣었다 뺄 수 있는 자료구조.
cnt = 0

while p:
    # 혼자남을경우 보트 주고 스탑!
    if len(p) == 1:
        cnt += 1
        break

    # 혼자서 limit이 넘을경우 보트 추가!
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    # 아닐경우 둘다 pop!
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)
