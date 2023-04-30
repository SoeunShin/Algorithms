# Programmers 120903. 배열의 유사도

"""
두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

입출력 예 #1
"b"와 "c"가 같으므로 2를 return합니다.

입출력 예 #2
같은 원소가 없으므로 0을 return합니다.
"""

def solution(s1, s2):
    return len([x for x in s1 if x in s2])

# return len(set(s1)&set(s2))
