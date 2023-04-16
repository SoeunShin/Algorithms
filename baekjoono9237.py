# 백준 9237. 이장님 초대

import sys
input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

for i in range(len(trees)):
    trees[i] += i + 1

print(max(trees) + 1)
