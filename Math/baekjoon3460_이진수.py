# 백준 3460. 이진수

"""
양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.
각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.
"""

import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(bin(n))[2:][::-1] # 13의 경우, 이진수가 0b1101로 생성되기 때문에, index 2부터 가져옴. 최하위 비트의 위치가 0 (=역순)이므로 [::-1]을 사용하여 reverse 해줌.

    idx_arr = [i for i in range(len(arr)) if arr[i]=='1']
    for i in idx_arr:
        print(i, end=' ')
