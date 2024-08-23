import sys

n = int(sys.stdin.readline())

for _ in range(n):
    n, m = map(int,sys.stdin.readline().split()) #n은 case 길이, m은 인덱스
    case = [int(k) for k in sys.stdin.readline().split()]
    
    count = 1
    while case :
        if case[0] < max(case): # 가장 큰값과 비교
            case.append(case.pop(0)) # 내 뒤에 가장 큰값이 있으면 맨뒤로 이동
        
        else: # 내가 가장 큰값일때
            if m == 0 : 
                break
            
            case.pop(0) # 가장 큰값 빼고
            count += 1 # 카운트 해주고
            
        if m > 0 : # 위에서 .pop() 한번 해준 이후
            m = m - 1  # 인덱스 조절
        else: # m 
            m = len(case) -1 

    print(count)
    