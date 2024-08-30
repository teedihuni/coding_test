# 미로 탐색
# https://www.acmicpc.net/problem/2178
#  (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
# 최소의 칸수는 bfs로 푸는게 베스트임

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append([int(k) for k in sys.stdin.readline().rstrip()])

def bfs(x,y):    
    queue = deque()
    queue.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n  and 0<=ny<m: # 범위 내부인 경우
        
                if graph[nx][ny] == 0 : # 갈수 없는 경우 
                    continue
                        
                if graph[nx][ny] == 1 : #처음 방문하는 경우만 계산
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
                    
    return graph[n-1][m-1]

print(bfs(0,0))
