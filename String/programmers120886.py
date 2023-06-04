# Programmers 120886. A를 B로 만들기

"""
문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

before	after	result
"olleh"	"hello"	1
"allpe"	"apple"	0
"""

def solution(before, after):
    before = sorted(list(before))
    after = sorted(list(after))
    return 1 if before==after else 0
