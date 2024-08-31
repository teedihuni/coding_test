# https://www.acmicpc.net/problem/1697
# 최단 경로 문제는 BFS 로 접근

from collections import deque

n, k = map(int,input().split())

visited =[0]*100001 # 방문을 기록할 리스트

def bfs(start,end):
    que = deque() 
    que.append((start,0)) # 시작점과 시간
    visited[start]=True
    
    while que:
        v, time = que.popleft()    
        
        if v==end: # 목적지 도착
            return time    
        
        for nv in (v-1, v+1, v*2):
            if 0<=nv<=100000 and not visited[nv]:
                visited[nv]=True
                que.append((nv,time+1))
                
print(bfs(n,k))
