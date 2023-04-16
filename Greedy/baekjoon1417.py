# 백준 1417. 국회의원 선거

import sys
input = sys.stdin.readline

n = int(input())
vote = []
cnt = 0 # 매수한 사람의 수 

for _ in range(n):
    vote.append(int(input()))

while (1):
    if (vote[0] == max(vote) and vote.count(max(vote)) == 1):
        break
    i = vote.index(max(vote), 1, n)
    vote[i] -= 1
    vote[0] += 1
    cnt += 1
    
print(cnt)
