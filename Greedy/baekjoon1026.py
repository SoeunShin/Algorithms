# 백준 1026. 보물

"""
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
B.reverse()
S = 0

for i in range(N):
    S += A[i]*B[i]

print(S)

# 메모리 31256
# 시간 44
# 코드 길이 210
