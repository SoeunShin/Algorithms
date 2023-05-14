# Softeer 금고털이

"""
루팡은 배낭을 하나 메고 은행금고에 들어왔다. 금고 안에는 값비싼 금, 은, 백금 등의 귀금속 덩어리가 잔뜩 들어있다. 배낭은 W ㎏까지 담을 수 있다.
각 금속의 무게와 무게당 가격이 주어졌을 때 배낭을 채울 수 있는 가장 값비싼 가격은 얼마인가?
루팡은 전동톱을 가지고 있으며 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다.

입력
100 2
90 1
70 2

출력
170
"""

import sys
input = sys.stdin.readline

w, n = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(n)]

jewels.sort(key = lambda x:x[1], reverse = True)

ans = 0
for weight, price in jewels:
    if w > weight:
        ans += weight * price
        w -= weight
    else:
        ans += w * price
        break

print(ans)
