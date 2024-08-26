import sys
from collections import deque

def is_vps(ps):
    stack = deque()
    
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:  # 스택이 비어있는데 ')'가 나오면 VPS가 아님
                return False
            stack.pop()
    
    # 스택이 비어있으면 모든 괄호가 짝을 이룬 것이므로 VPS
    return len(stack) == 0

number = int(sys.stdin.readline())

for _ in range(number):
    ps = sys.stdin.readline().rstrip()
    if is_vps(ps):
        print('YES')
    else:
        print('NO')