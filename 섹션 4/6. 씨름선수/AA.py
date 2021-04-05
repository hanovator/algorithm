import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
body = []

for i in range(n):
    # 키와 몸무게
    a, b = map(int, input().split())
    body.append((a, b))

# 키 기준으로 내림차순 정렬
body.sort(reverse=True)
largest = 0
cnt = 0

# 몸무게 최대가 갱신되는 때가 선수를 뽑을 수 있는 조건!
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)
