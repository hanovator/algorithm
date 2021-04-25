import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum, tsum):
    global result  # result는 global 변수로 사용하고 있으므로 global을 사용한다.
    print('L -- ', L)
    print('sum -- ', sum)
    print('tsum -- ', tsum)
    print('(total - tsum) -- ', (total - tsum))
    print('sum + (total - tsum) -- ', sum + (total - tsum))
    print('result -- ', result)
    print()

    if sum + (total - tsum) < result:  # tree밑 남은 값들의 합이 result(현재 최대값)보다 작다면 out!
        return
    if sum > c:  # sum이 무게제한이상이라면 return
        return
    if L == n:  # 말단노드까지 왔을때.
        if sum > result:
            result = sum  # 더 큰 sum으로 result 변경.
    else:
        print('tsum2222 -- ', tsum)
        print()

        # tsum은 global변수가 아니다!
        DFS(L + 1, sum + a[L], tsum + a[L])  # l+1번째 바둑이를 태운다!
        DFS(L + 1, sum, tsum + a[L])  # l+1번째 바둑이를 태우지 않는다!


if __name__ == "__main__":
    # c: 무게제한, n: 바둑이 마리수.
    c, n = map(int, input().split())
    a = [0] * n  # 바둑이 각각의 무게.
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
