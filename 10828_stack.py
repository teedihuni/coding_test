order_cnt = int(input())
stack = []

def preprocess(order, stack):
   
    if order == 'top':
        if stack:
            num = stack[-1]
            print(num) 
        else:
            print(-1) 
            
    elif order == 'pop':
        if stack :
            num = stack[-1]
            stack = stack[:-1]
            print(num) 
        else:
            print(-1)  
            
    elif order == 'size':
        print(len(stack)) 
        
    elif order == 'empty':
        if stack:
            print(0) 
        else:
            print(1) 
            
    else:
        order, num = order.split(' ')
        if order == 'push':
            stack.append(int(num))
            
for i in range(order_cnt):
    order = str(input())
    preprocess(order, stack)
