import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum):
    # if sum > total // 2:  # 총합의 절반이상을 넘어간다면 값이 같을 수 없으므로 return
    #     return
    # L: tree의 level을 의미.
    print('sum -- ', sum)
    print('level -- ', L)
    print()
    if L == n:  # 마지막 level까지 왔다면.

        if sum == (total - sum):  # 내가 만든 부분집합과 그렇지 않은 부분집합의 크기가 같다면.
            #print('sum3 -- ', sum)
            print("YES")
            sys.exit(0)  # 프로그램 종료.
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
