import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
meeting = []

for i in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))

# 뒷부분을 기준으로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0

# x: 회의의 앞시간
# y: 회의의 뒷시간
for x, y in meeting:

    # 회의의 앞시간이 endpoint보다 크거나 같다면?
    if x >= et:
        et = y
        cnt += 1

print(cnt)
