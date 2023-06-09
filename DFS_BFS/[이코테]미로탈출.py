# [이코테] 미로 탈출

"""
N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다. 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다.
다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 항상 1이다.

예제 1

입력:
5 6
101010
111111
000001
111111
111111

출력:
10
"""
import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 상하좌우 이동 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 0: # 괴물 
                continue

            # 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 해당 노드까지의 최단거리 기록 
                queue.append((nx, ny))

    return graph[n-1][m-1] # 출구까지의 최단거리 반환 (출구 위치에 적혀있는 거리가 탈출 시 최단거리)

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
