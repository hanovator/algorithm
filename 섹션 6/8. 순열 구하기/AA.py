import sys

sys.stdin = open("in1.txt", "r")


def DFS(L):
    global cnt
    if L == m:  # level이 뽑아야 할 구슬수(m)만큼 들어왔을때.
        for i in range(m):
            print(res[i], end=' ')  # res에 들어있던 결과값을 출력.
        print()
        cnt += 1
    else:
        # i는 가지를 뜻한다.
        for i in range(1, n + 1):  # 구슬수만큼 가지를 친다.
            # ch==0 즉 아직 뽑히지 않은것이라면.
            if ch[i] == 0:  # 배열 안의 값을 바꾸는 것이라면 global을 해줄 필요 없다.
                ch[i] = 1  # 뽑힌 가지임을 체크.
                res[L] = i  # 결과에 저장.

                ##### 윗부분은 DFS전에 적용한것
                DFS(L + 1)
                ##### 밑부분은 해당 DFS가 종료 후 적용할것.

                ch[i] = 0 # level이 올라갈때 해당 가지 ch를 초기화.


if __name__ == "__main__":
    n, m = map(int, input().split())  # n: 총구슬, m: 뽑을구슬.
    res = [0] * m  # 2개만 뽑을것이므로 2개의 공간만 있으면 된다.
    ch = [0] * (n + 1)  # check할 list.
    cnt = 0
    DFS(0)
    print(cnt)
