# Softeer 장애물 인식 프로그램

"""
자율주행팀 SW 엔지니어인 당신에게 장애물과 도로를 인식할 수 있는 프로그램을 만들라는 업무가 주어졌다.
우선 [그림 1]과 같이 정사각형 모양의 지도가 있다. 1은 장애물이 있는 곳을, 0은 도로가 있는 곳을 나타낸다.
당신은 이 지도를 가지고 연결된 장애물들의 모임인 블록을 정의하고, 불록에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 장애물이 좌우, 혹은 아래위로 붙어 있는 경우를 말한다. 대각선 상에 장애물이 있는 경우는 연결된 것이 아니다.
[그림 2]는 [그림 1]을 블록 별로 번호를 붙인 것이다.
지도를 입력하여 장애물 블록수를 출력하고, 각 블록에 속하는 장애물의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
7
1110111
0110101
0110101
0000100
0110000
0111110
0110000

출력
3
7
8
9
"""

import sys
input = sys.stdin.readline

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0

    if graph[x][y] == 1:
        graph[x][y] = 0

        cnt = 1
        cnt += dfs(x+1, y)
        cnt += dfs(x-1, y)
        cnt += dfs(x, y+1)
        cnt += dfs(x, y-1)
        return cnt

    return 0

n = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

obs_cnt = []

for i in range(n):
    for j in range(n):
        cnt = dfs(i,j)
        if cnt > 0:
            obs_cnt.append(cnt)

print(len(obs_cnt))
obs_cnt.sort()
for i in obs_cnt:
    print(i)
