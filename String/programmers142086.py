# Programmers 142086. 가장 가까운 같은 글자

"""
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
"""

def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] not in s[:i]: # 자신의 앞에 같은 글자가 없을 때
            answer.append(-1)
        else: # 자신의 앞에 같은 글자가 있을 때
            cnt = 1
            for j in range(1, i+1): # 자신의 앞에 있는 글자를 하나씩 확인 
                if s[i-j] != s[i]: # 해당 글자가 자신과 같지 않으면 
                    cnt += 1
                else: # 자신과 같으면 
                    answer.append(cnt)
                    break
            
    return answer

"""
개선점: for문을 2번 사용하지 않고도 구현할 수 있다. 실행 시간을 줄이기 

다른 사람의 풀이
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic: # 처음 나온 글자를 dic에 저장 
            answer.append(-1) # 처음 나왔기 때문에 자신과 동일한 글자가 없으므로 -1 추가 
        else: # 이미 자신과 동일한 글자가 dic에 존재할 때
            answer.append(i - dic[s[i]]) # 현재 index와 dic에 저장된 index의 차를 추가 
        dic[s[i]] = i # 가장 늦게 나온 글자의 index로 수정

    return answer
"""
