# Programmers 120902. 문자열 계산하기

"""
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

입출력 예 #1
3 + 4 = 7을 return 합니다.
"""

def solution(my_string):
    arr = my_string.split()
    ans = int(arr[0])
    for i in range(1, len(arr), 2):
        if arr[i] == '+':
            ans += int(arr[i+1])
        else:
            ans -= int(arr[i+1])
    return ans

# return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
