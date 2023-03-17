# 백준 7568. 덩치

"""
A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.

N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다. 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.
이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.

첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = []
level = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    level.append(cnt + 1)

for i in level:
    print(i, end=' ')

# 메모리 31256
# 시간 40
# 코드 길이 355

