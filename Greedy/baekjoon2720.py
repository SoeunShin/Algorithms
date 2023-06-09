# 백준 2720. 세탁소 사장 동혁

"""
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.

예제 1

입력:
3
124
25
194

출력:
4 2 0 4
1 0 0 0
7 1 1 4
"""

import sys
input = sys.stdin.readline

n = int(input())

coin = [25, 10, 5, 1]

for i in range(n):
    ans = []
    money = int(input())
    for c in coin:
        ans.append(str(money//c))
        money %= c
    print(" ".join(ans))
