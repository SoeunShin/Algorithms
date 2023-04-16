# 백준 2810. 컵홀더

import sys
input = sys.stdin.readline

n = input()
seat = input()
cnt = 0

couple = seat.count('LL')
single = seat.count('S')

if couple > 0:
    cnt += couple + 1 # 1개 - 2명, 2개 - 3명, 3개 - 4명 ...
cnt += single

print(cnt)
