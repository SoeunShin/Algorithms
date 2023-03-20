# 백준 15904. UCPC는 무엇의 약자일까?

"""
문자열이 주어지면 이 문자열을 적절히 축약해서 "UCPC"로 만들 수 있는지 확인하는 프로그램을 만들어보자.
축약이라는 것은 문자열에서 임의의 문자들을 제거하는 행동을 뜻한다. 예를 들면, "apple"에서 a와 e를 지워 "ppl"로 만들 수 있고,
"University Computer Programming Contest"에서 공백과 소문자를 모두 지워 "UCPC"로 만들 수 있다.
문자열을 비교할 때는 대소문자를 구분해 정확히 비교한다. 예를 들어 "UCPC"와 "UCpC"는 다른 문자열이다.
따라서 "University Computer programming Contest"를 "UCPC"로 축약할 수 있는 방법은 없다.

예제
입력: Union of Computer Programming Contest club contest
출력: I love UCPC

입력: University Computer Programming
출력: I hate UCPC
"""

import sys
input = sys.stdin.readline

st = input()
arr = ['U', 'C', 'P', 'C']
check = 1

for i in range(4):
    if arr[i] in st:
        idx = st.index(arr[i])
        st = st[idx+1:]
    else:
        check = 0
        break

if check == 1:
    print("I love UCPC")
else:
    print("I hate UCPC")
