# https://www.acmicpc.net/problem/1405

from functools import reduce
N, e, w, s, n = map(int,input().split())

directions = [(i/100) for i in [e,w,s,n]]
graph = [[0]*50 for i in range(50)]

moving_count = 0
way_list = []
result = 0

def robot(x,y):
    graph[x][y]=1
    global moving_count, result
    if moving_count == N:
        result += reduce(lambda x, y : x*y, way_list) # 리스트 내의 모든 값의 곱
        return
        
    dx = [0,0,1,-1] #e, w, s, n
    dy = [1,-1,0,0]
    
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if graph[new_x][new_y]==0: # 아직 미방문
            way_list.append(directions[i])
            moving_count += 1
            robot(new_x,new_y) #재귀
            way_list.pop() # 최근 방문 위치 초기화
            graph[new_x][new_y]=0
            moving_count -=1
            
robot(25,25)
print(f"{result:.9f}")