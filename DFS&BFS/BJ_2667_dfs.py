# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667


import sys

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
count = 0

def dfs(x,y):
    global count
    
    if x < 0 or x >= n or y < 0 or y >= n : # 영역 밖에 대한 조건 설정
        return False
    
    if graph[x][y]==1 :
        count += 1 # 단지 영역에 대한 크기 설정
        graph[x][y]=0 # 방문한 곳 0으로 변경
        
        for i in range(4): # 4방향 이동
            X = x + dx[i]
            Y = y + dy[i]
            dfs(X,Y)
        return True
    return False

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(count)
            count = 0 # 1인곳 영역 다 끝나면 초기화
            
result.sort() #오름차순

print(len(result))
for k in result:
    print(k)
    
    
