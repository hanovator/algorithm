import sys

sys.stdin = open("in1.txt", "r")  # 35+2*
a = input()
stack = []

for x in a:
    if x.isdecimal():  # 숫자인지 확인.
        stack.append(int(x))  # 숫자인경우 stack에 넣는다(계산 가능하도록 int로 casting).
    else:
        # 전 두개의 숫자를 stack에서 빼서 숫서를 바꿔준 후 연산.
        if x == '+':  
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)

print(stack[0])
