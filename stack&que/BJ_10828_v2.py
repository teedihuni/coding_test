import sys
order_count = int(sys.stdin.readline())

stack = []
for i in range(order_count):
    order = sys.stdin.readline().split()

    if order[0] == 'top':
        if stack:
            num = stack[-1]
            print(num) 
        else:
            print(-1) 
            
    elif order[0] == 'pop':
        if stack :
            num = stack.pop()
            print(num) 
        else:
            print(-1)  
            
    elif order[0] == 'size':
        print(len(stack)) 
        
    elif order[0] == 'empty':
        if stack:
            print(0) 
        else:
            print(1) 
            
    elif order[0] == 'push':
        num = order[1]
        stack.append(int(num))
            

