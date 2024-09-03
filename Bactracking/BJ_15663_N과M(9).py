# N과 M (9)
# https://www.acmicpc.net/problem/15663
n, m = map(int, input().split())

num_list = sorted(list(map(int,input().split())))

result = []
visited = [False]*n  # 사용한 숫자에 대한 기록

def dfs():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    
    remember_me = 0 # 
    
    for i in range(n):
        if not visited[i] and remember_me != num_list[i]: # 조건 설정
            visited[i] = True
            result.append(num_list[i])
            remember_me = num_list[i]
            dfs()
            visited[i]=False
            result.pop()

dfs()
