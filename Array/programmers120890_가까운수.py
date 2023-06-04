# Programmers 120890. 가까운 수

"""
정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

array	n	result
[3, 10, 28]	20	28
[10, 11, 12]	13	12
"""

def solution(array, n):
    array.sort()
    diff = n
    idx = 0
    for i in range(len(array)):
        if abs(n-array[i]) < diff:
            diff = abs(n-array[i])
            idx = i       
    return array[idx]

"""
array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
"""
