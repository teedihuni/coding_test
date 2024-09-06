#https://www.acmicpc.net/problem/1759

L, C = map(int,input().split())
letter = sorted(list(input().split()))

result = []
mo_count = 0 # 모음 카운트
ja_count = 0 # 자음 카운트 

def solution(idx):
    global mo_count, ja_count
    
    if len(result)==L and mo_count>=1 and ja_count>=2: # 암호 최소조건
        print(''.join(result))
        return
    
    for i in range(idx,len(letter)):
        c = letter[i]
        if c in ['a','e','i','o','u']:   
            mo_count+=1
            result.append(c)
            solution(i+1)
            result.pop()
            mo_count-=1
        else:
            ja_count+=1
            result.append(c)
            solution(i+1)
            result.pop()
            ja_count-=1
            
solution(0)
        


