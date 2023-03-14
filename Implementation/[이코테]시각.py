# [이코테] Ch 4. 구현 - 4-2. 시각
# 완전 탐색 (Brute Forcing)

"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 구하는 프로그램을 작성하라. 예를 들어 1을 입력했을 때
다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이다

00시 00분 03초
00시 13분 30초
반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각이다

00시 02분 55초
01시 27분 45초
"""

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                cnt += 1
print(cnt)
