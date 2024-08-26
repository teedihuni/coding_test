import sys

def is_vps(ps):
    count = 0
    
    for char in ps:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        # 중간에 count가 음수가 되면 VPS가 될 수 없음
        if count < 0:
            return False
    
    # 모든 괄호를 처리한 후 count가 0이면 VPS
    return count == 0

number = int(sys.stdin.readline())

for _ in range(number):
    ps = sys.stdin.readline().rstrip()
    if is_vps(ps):
        print('YES')
    else:
        print('NO')