# 백준 11399. ATM

"""
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted((list(map(int, input().split()))))
time = 0

for i in range(N):
    time += sum(arr[:i+1])
        
print(time)

# 메모리 31256
# 시간 48
# 코드 길이 180
