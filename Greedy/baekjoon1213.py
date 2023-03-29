# 백준 1213. 팰린드롬 만들기

"""
임한수와 임문빈은 서로 사랑하는 사이이다.
임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에,
둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데,
임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

입력
AABB
출력
ABBA

입력
ABCD
출력
I'm Sorry Hansoo
"""

import sys
input = sys.stdin.readline

name = input().rstrip()
dic = dict()

for c in name:
    if dic.get(c) == None:
        dic[c] = 1
    else:
        dic[c] += 1

odd = ''
for k, v in dic.items():
    if v % 2 == 1: # 홀수
        if len(odd) > 0:
            print("I'm Sorry Hansoo")
            break
        odd = k
else:
    ans = ''
    for k, v in sorted(dic.items()):
        ans += k * (v//2)
    ans += odd + ans[::-1]
    print(ans)
