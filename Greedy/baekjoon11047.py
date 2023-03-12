# 백준 11047. 동전 0

"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""

import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
cnt = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr = reversed(sorted(arr))

for coin in arr:
    cnt += K//coin
    K %= coin

print(cnt)

# 메모리 31256 KB
# 시간 44 ms
# 코드 길이 228 B
