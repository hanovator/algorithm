import sys

sys.stdin = open("in1.txt", "r")  # (3+5)*2
a = input()
stack = []
res = ''  # 정답 누적.

for x in a:
    if x.isdecimal():  # 숫자인지 확인.
        res += x
    else:
        if x == '(':  # 여는 괄호는 무조건 append.
            stack.append(x)
        elif x == '*' or x == '/':
            # 자기보다 연산순위가 같거나 빠른 연산들을 stack에서 빼내어 먼저 계산될 수 있게 res에 붙여준다.
            # + or -의경우 * or / 보다 연산 우선순위가 낮으므로 stack에서 빼주고 그 위로 stack을 쌓는다.
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # + or -의 경우 자기보다 모두 연산이 빠르므로 (가 아닌한 모두 빼서 res에 붙여준다.
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            # 마지막 여는괄호 pop() * 닫는괄호가 있다면 여는괄호도 있다.
            stack.pop()

while stack:
    res += stack.pop()

print(res)
