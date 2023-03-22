# [이코테] 위에서 아래로

"""
하나의 수열에는 다양한 수가 존재하며, 이런 큰 수는 크기와 상관 없이 무작위로 주어진다.
이 수를 큰수 부터 작은 수까지 내림차순으로 정렬하면되는 문제다.
즉 수열을 내림차순으로 정렬하는 프로그램을 만들면된다.

예제

입력:
3
15
27
12

출력:
27 15 12
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for i in sorted(arr):
    print(i, end=' ')
