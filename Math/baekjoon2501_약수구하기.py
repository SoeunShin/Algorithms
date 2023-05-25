# 백준 2501. 약수 구하기 

"""
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

입력
6 3
출력
3

입력
25 4
출력
0

입력
2735 1
출력
1
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [i for i in range(1,n+1) if n%i == 0]

if len(arr) < k:
    print(0)
else: print(arr[k-1])
