# [이코테] Ch 4. 구현 - 4-1. 상하좌우

"""
여행가 A는 N × N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 × 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가
이동할 계획이 적힌 계획서가 놓여 있다

계획서에는 하나의 줄에 띄어쓰기를 기준으로 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = input().split()

x, y = 1, 1

types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for p in arr:
    for i in range(len(types)):
        if p == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx > n or ny > n or nx < 1 or ny < 1:
        continue
    x, y = nx, ny
    
print(x, y)
