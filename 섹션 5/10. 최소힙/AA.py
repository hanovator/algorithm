import sys
import heapq as hq   # heapq: 최소힙.

sys.stdin = open("in1.txt", "r")
a = []

while True:
    n = int(input())
    print('n -- ', n)
    print('a -- ', a)
    if n == -1:  # n값이 -1일경우는 맨 끝을 뜻함으로 break.
        break
    if n == 0:  # 0이 입력되면 현재 최소힙에서 최소값을 꺼내어 출력.
        if len(a) == 0:  # heap 자료구조에 값이 없는경우.
            print(a)
            print(-1)
        else:  # heap 자료구조에 값이 있는경우.
            print()
            print('pop -- ', hq.heappop(a))  # 최소값 출력!
    else:
        hq.heappush(a, n)
        print('heappush -- ', a)
    print('==============')
