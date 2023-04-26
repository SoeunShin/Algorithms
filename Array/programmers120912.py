# Programmers 120912.7의 개수

"""
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

입출력 예 #1
[7, 77, 17]에는 7이 4개 있으므로 4를 return 합니다.

입출력 예 #2
[10, 29]에는 7이 없으므로 0을 return 합니다.
"""

def solution(array):
    array = list(map(str, array))
    return (''.join(n for n in array)).count('7')
