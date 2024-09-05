# https://www.acmicpc.net/problem/1182

# 변수 입력 

from collections import deque
n, s = map(int, input().split())
num_list = sorted(list(map(int,input().split())))

print(num_list)
result = deque()

count = 0 # 수열합 되는 개수

def solution(i):
    global count
    
    if sum(result) == s and result: # 아무것도 없는 경우는 제외
        count+=1
    
    for k in range(i, len(num_list)):
        result.append(num_list[k]) 
        solution(k+1) # 다음 idx 부터 시작하도록 
        result.pop() # 합이 s가 아닐때 재귀함수 종료되니까 마지막에 추가한거 빼주기

solution(0)