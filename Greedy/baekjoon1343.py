# 백준 1343. 폴리오미노

"""
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다.
이때, '.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

예제
입력: XXXXXX
출력: AAAABB

입력: XX.XX
출력: BB.BB

입력: XXXX....XXX.....XX
출력: -1
"""

import sys
input = sys.stdin.readline

st = input()
st = st.replace('XXXX', 'AAAA')
st = st.replace('XX', 'BB')

if 'X' in st:
    print(-1)
else:
    print(st)
