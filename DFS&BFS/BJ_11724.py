# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque
sys.setrecursionlimit(2000) 
n,m = map(int, sys.stdin.readline().rstirp().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [False]*(n+1)
#print(graph)

## DFS
def dfs(visited, start):
    visited[start]=True
    case = sorted(graph[start])
    for i in case:
        if not visited[i]:
            dfs(visited,i)

    
for i in range(n):
    if not visited[i+1]: # 함수 진입 조건
        dfs(visited, i+1)
        count+=1
        
print(count)


## BFS 
def bfs(visited, start):
    queue = deque([start]) # 시작 넣어주고
    visited[start]=True # 방문한곳 처리
    
    while queue:
        v = queue.popleft() #처음 방문한곳 제거
        for i in sorted(graph[v]):
            if not visited[i]: # 방문안한곳
                queue.append(i) # 추가 
                visited[i] = True # 방문 처리
    
for i in range(n):
    if not visited[i+1]: # 함수 진입 조건
        bfs(visited, i+1)
        count+=1
        
print(count)

    