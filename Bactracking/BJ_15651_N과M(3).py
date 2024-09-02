# N과 M(3)
# https://www.acmicpc.net/problem/15651

n, m = map(int,input().split())

s = []

def dfs():
    if len(s) == m: # 정해진 개수가 도달하면 
        print(' '.join(map(str,s))) # 출력
        return # 함수 종료
     
    for i in range(1,n+1): # 정해진 n 범위까지 for문 돌면서 
        s.append(i) # 추가 
        dfs() # 다시 함수 진입
        s.pop() # 함수 종료되어 나오면 이전에 추가했던거 삭제
        
dfs()
