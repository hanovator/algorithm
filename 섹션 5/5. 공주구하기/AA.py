import sys
from collections import deque

sys.stdin = open("in1.txt", "r")  # 20 3
n, k = map(int, input().split())
q = list(range(1, n + 1))

# popleft로 가장 왼쪽의 값을 pop 시킨다.
# append로 오른쪽에 값을 input 시킨다.
dq = deque(q)


while dq:
    # k가 3 이라면 2번 맨뒤의 숫자를 앞으로 붙여주며 원처럼 만들어준다.
    # k가 3이기 때문데 2번 맨뒤 숫자를 앞으로 붙여준다.
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
