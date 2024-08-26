import sys
from collections import deque

number = int(sys.stdin.readline())

for i in range(number):
    ps = deque(sys.stdin.readline().rstrip()) # 괄호 문자열    
    tmp = deque() 

    valid = True
    while ps:
        tmp.append(ps.popleft())
        if tmp[0] == ")" or ps[-1] == "(": # 시작과 끝이 아예 매칭될 수 없는 조건인 경우
            valid = False
            break
        
        while tmp[-1] != ps[0]:
            tmp.pop()
            ps.popleft()
                
            if len(ps) == 0 or len(tmp) == 0:
                    break

    if valid and len(tmp)==0 :
        print('YES')
    else: 
        print('NO')