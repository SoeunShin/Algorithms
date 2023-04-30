# Programmers 120899. 가장 큰 수 찾기

"""
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

입출력 예 #1
1, 8, 3 중 가장 큰 수는 8이고 인덱스 1에 있습니다.

입출력 예 #2
9, 10, 11, 8 중 가장 큰 수는 11이고 인덱스 2에 있습니다.
"""

def solution(array):
    m = max(array)
    return [max(array), array.index(m)]
