import sys
sys.setrecursionlimit(10000000) 

case_num = int(input())



def dfs(x,y): # 함수 정의
    
    graph[x][y] = 0 # 방문처리
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
     
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if 0<=new_x<m and 0<=new_y<n: # 범위 설정
            if graph[new_x][new_y]: # 아직 방문 x 
                dfs(new_x,new_y)
                
# case_num 설정
for _ in range(case_num):
    # 초기 입력 세팅
    m, n, k = map(int,sys.stdin.readline().split())
    # 그래프 입력
    graph = [[0]*n for _ in range(m)]
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    
    # count 정의
    count = 0
    
    # 조건 설정    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                dfs(i,j)
                count +=1

    print(count)