import sys

sys.stdin = open("in1.txt", "r")


def Count(capacity):
    cnt = 1  # DVD 개수
    sum = 0

    for x in Music:
        if sum + x > capacity:  # sum + x가 용량을 초과할경우 더해주지 않고 다음 DVD로 넘어가야 한다.
            cnt += 1
            sum = x
        else:  # 용량을 초과하지 않을경우 sum으로 DVD에 들어갈 노래의 길이들을 더해준다.
            sum += x

    return cnt  # cnt가 m 이상일경우 탈락!


# n: DVD에 들어가는 곡의 개수
# m: 사용해야할 DVD의 개수
n, m = map(int, input().split())
Music = list(map(int, input().split()))  # 각노래의 길이(분)들이 들어있다.
max = max(Music)

lt = 1
rt = sum(Music)  # 최대 한 DVD에 들어갈 수 있는 노래의 길이 개수
res = 0  # DVD 한장에 최소한의 용량이 들어간 분의 길이

while lt <= rt:

    mid = (lt + rt) // 2  # 이분검색(가운데 값을 먼저 구한다.)

    # 이분검색 시작!
    if Count(mid) <= m:  # 사용한 DVD의 개수가 m보다 작아야한다.
        res = mid  # 이분검색을 하다가 더 작은값이(더 좋은값)나오면 갱신한다.
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
