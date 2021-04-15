import sys

sys.stdin = open("in1.txt", "r")

a = input()  # 첫번째 문자나열.
b = input()  # 두번째 문자나열.

str1 = dict()  # 첫번째 문자나열을의 각 문자 개수를 넣을 dict.
str2 = dict()  # 두번째 문자나열을의 각 문자 개수를 넣을 dict.

# 각문자가 몇개 들어있는지 보기위해 dict에 넣는다.
for x in a:
    # str1.get(x, 0): x값이 없으면 0을 반환, 있으면은 해당값을 반환.
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

# 서로의 구성성분이 다 같은지 확인.
for i in str1.keys():
    if i in str2.keys():  # str1의 각 key값은 str2에 포함되어있어야 한다.
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
