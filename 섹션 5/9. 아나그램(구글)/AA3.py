import sys

sys.stdin = open("in1.txt", "r")
a = input()
b = input()
str1 = [0] * 52  # 알파벳  대문자 26개, 소문자 26개
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # 대문자 알파벳의경우 65부터 시작함으로 65를 빼준다.
    else:
        str1[ord(x) - 71] += 1  # 소문자 알파벳의경우 97부터 시작함으로 27부터 시작하기 위해 71을 빼준다.

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

# 두 리스트를 비교하여 완전히 같은지 비교.
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
