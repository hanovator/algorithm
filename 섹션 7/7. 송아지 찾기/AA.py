import sys
from collections import deque

sys.stdin = open("in1.txt", "r")

MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)

n, m = map(int, input().split())  # n: 출발점, m: 도착점
ch[n] = 1  # 출발점 check!
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:  # dQ가 비어있으면 멈춤
    print('dQ -- ', dQ)
    now = dQ.popleft()
    print('dQ2 -- ', dQ)
    print('ch -- ', ch)
    print('now -- ', now)
    print('dis -- ', dis)
    print()

    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):  # now-1, now+1, now+5 차례로 3바퀴를 돈다. (3개의 가지를 친다!)
        if 1 <= next <= MAX:
            if ch[next] == 0:  # 방문을 안했을경우
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])