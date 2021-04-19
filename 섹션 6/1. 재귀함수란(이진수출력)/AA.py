import sys

sys.stdin = open("in1.txt", "r")


# 재귀함수.
# - 스택에 스텍프레임 형태로(매개변수, 지역변수, 복귀주소) 저장된다.
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)  # 나눗셈의 목을 반환한다.
        print(x % 2, end='')  # 나눗셈의 나머지를 출력한다.


n = int(input())
DFS(n)
