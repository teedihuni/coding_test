# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667


import sys
from collections import deque

n = int(sys.stdin.readline())

# 그래프 입력
graph = [[] for _ in range(n)]
for i in range(n):
    line = [int(str) for str in sys.stdin.readline().rstrip()]
    graph[i] = line
    
# DFS
# 이동할 방향
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, a , b): # 좌표가 1인 경우 실행될 거임
    queue = deque() #큐 선언
    queue.append([a,b])
    graph[a][b] = 0  # 첫번쨰 집 방문 처리
    count = 1 # 첫번째 영역 시작
    
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            
            if graph[nx][ny] == 1: # 이동한 위치가 아직 방문 안했으면
                graph[nx][ny] = 0 # 방문한 곳 0
                queue.append([nx,ny]) # 이동한 좌표 추가
                count += 1
    return count

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(graph, i ,j)
            result.append(count)
            
result.sort()

print(len(result))
for k in result:
    print(k)