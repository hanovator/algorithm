import sys

sys.stdin = open("in1.txt", "r")
s = input()
stack = []
cnt = 0  # stack 안에있응 '('를 다 더해준다.

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
