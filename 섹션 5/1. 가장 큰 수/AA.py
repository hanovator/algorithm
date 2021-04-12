import sys

sys.stdin = open("in1.txt", "rt")
num, m = map(int, input().split())
print(num)

num = list(map(int, str(num)))
print(num)

stack = []

for x in num:

    # stack이 비어있지 않고 m(제거할 개수)이 0보다 크고 stack안의 숫자보다 현재 x의 값이 더 크다면
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1

    stack.append(x)

# 제거해야할 개수를 전부 쓰지 못한경우
if m != 0:
    # 끝 마지막부분을 제거!
    stack = stack[:-m]

res = ''.join(map(str, stack))

print(res)
