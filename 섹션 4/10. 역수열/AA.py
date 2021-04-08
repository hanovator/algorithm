import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n

print('a -- ', a)

for i in range(n):
    for j in range(n):

        # a: 현재 역수열의 값
        # seq: 원수열 (역수열 되기 전의 수열)
        # 역수열의 값이 0이고, 정수열의 값이 0 이라면 i + 1의 seq배열자리에 값을 넣는다.
        if a[i] == 0 and seq[j] == 0:
            print('i  -- ', i)
            print('j  -- ', j)
            seq[j] = i + 1
            break
        # seq(원수열)에 이미 값이 차있다면(!=0) 그 뒤에 값을 넣어주어야 한다.
        elif seq[j] == 0:
            a[i] -= 1
            print('a[i]  -- ', a[i] )

    print('===================')

for x in seq:
    print(x, end=' ')
