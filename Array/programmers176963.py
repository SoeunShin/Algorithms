# 추억 점수

"""
입출력 예 #1
첫 번째 사진 속 "may", "kein", "kain", "radi"의 그리움 점수를 합치면 19(5 + 10 + 1 + 3)점 입니다. 
두 번째 사진 속 그리워하는 사람들인 "may"와 "kein"의 그리움 점수를 합치면 15(5 + 10)점입니다. 
세 번째 사진의 경우 "kain"과 "may"만 그리워하므로 둘의 그리움 점수를 합한 6(1 + 5)점이 사진의 추억 점수입니다. 따라서 [19, 15, 6]을 반환합니다.

입출력 예 #2
첫 번째 사진 속 그리워하는 사람들인 "kali", "mari", "don"의 그리움 점수를 합치면 67(11 + 1 + 55)점입니다. 
두 번째 사진 속엔 그리워하는 인물이 없으므로 0점입니다. 
세 번째 사진 속 그리워하는 사람은 "don"만 있으므로 55점입니다. 따라서 [67, 0, 55]를 반환합니다.
"""

def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    ans = []
    for arr in photo:
        tmp = 0
        for n in arr:
            if n in name:
                tmp += dic[n]
            else: pass
        ans.append(tmp)
    return ans
