import sys

n = int(sys.stdin.readline())

for i in range(n):
    n, m = map(int,sys.stdin.readline().split()) #n은 case 길이, m은 인덱스
    case = [int(k) for k in sys.stdin.readline().split()]
    
    result = 1
    while case :
        if case[0] < max(case):
            case.append(case.pop(0))
        
        else:
            if m == 0 : 
                break
            
            case.pop(0)
            result += 1
            
        if m > 0 : 
            m = m - 1  #인덱스 조절
        else:
            m = len(case) -1 

    print(result)
    