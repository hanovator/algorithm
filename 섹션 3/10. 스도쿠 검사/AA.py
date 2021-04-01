import sys

sys.stdin = open("in1.txt", "r")


def check(a):
    for i in range(9):
        ch1 = [0] * 10  # 행을 체크.
        ch2 = [0] * 10  # 열을 체크.
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:  # 하나라도 중복이 있는경우 false.
            return False

    # 3*3 그룹탐색.
    for i in range(3):  # 3*3 그룹 행
        for j in range(3):  # 3*3 그룹 열
            ch3 = [0] * 10  # 그룹체크
            for k in range(3):  # 그룹안에 행
                for s in range(3):  # 그룹안에 열
                    ch3[a[i * 3 + k][j * 3 + s]] = 1  # 그룹은 3칸씩 띄어져있으므로 3을 곱한다.
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
print(a)

if check(a):
    print("YES")
else:
    print("NO")
