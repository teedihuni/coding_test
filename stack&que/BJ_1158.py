import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

circle = deque([i for i in range(1,n+1)])
rotation_num = k-1

result = '<'

for i in range(n):
    circle.rotate(-rotation_num)
    pop_num = circle.popleft()
    result += f'{pop_num}, '

result = result[:-2]
result += '>'

print(result)

#  메모리 효율성 개선가능한 부분
result = []

for _ in range(n):
    circle.rotate(-rotation_num)
    pop_num = circle.popleft()
    result.append(str(pop_num))

print(f"<{', '.join(result)}>")