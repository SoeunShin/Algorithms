# 백준 4949. 균형잡힌 세상

"""
모든 왼쪽 소괄호("(")는 오른쪽 소괄호(")")와만 짝을 이뤄야 한다.
모든 왼쪽 대괄호("[")는 오른쪽 대괄호("]")와만 짝을 이뤄야 한다.
모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
모든 괄호들의 짝은 1:1 매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.
정민이를 도와 문자열이 주어졌을 때 균형잡힌 문자열인지 아닌지를 판단해보자.

각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.

각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

입력 
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

출력 
yes
yes
no
no
no
yes
yes
"""

import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s =='.':
        break
    
    stack = []
    result = True

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack[-1] == '[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif c == ']':
            if len(stack) == 0 or stack[-1]=='(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if len(stack)==0 and result==True:
        print('yes')
    else:
        print('no')
