# DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

dot, lines, start_point = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(dot+1)]

for _ in range(lines):
    i, j = map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph, start_point, visited):
    
    visited[start_point] = True
    print(start_point, end=' ')
    searching_area = sorted(graph[start_point])
    for i in searching_area:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start_point, visited):
    queue = deque([start_point])
    visited[start_point] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i]=True
        
    
visited = [False]*(dot+1)
dfs(graph, start_point, visited)
print()
visited = [False]*(dot+1)
bfs(graph, start_point, visited)

