import sys

sys.stdin = open("in1.txt", "r")
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

# sh dict에 넣어줬던 값들을 다시 원상복구 해 준다.
for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    # 만약 원상복구 되지 않은 문자가 있다면 NO!
    if sH.get(x) > 0:
        print("NO")
        break;
else:
    print("YES")
