order_cnt = int(input())
stack = []

def preprocess(order, stack):
   
    if order == 'top':
        if stack:
            num = stack[-1]
            return stack, num
        else:
            return stack, -1
            
    elif order == 'pop':
        if stack :
            num = stack[-1]
            stack = stack[:-1]
            return stack, num
        else:
            return stack , -1
            
    elif order == 'size':
        return stack, len(stack)
        
    elif order == 'empty':
        if stack:
            return stack, 0
        else:
            return stack, 1
            
    else:
        order, num = order.split(' ')
        if order == 'push':
            stack.append(int(num))
            return stack, False

results = []
for i in range(order_cnt):
    order = str(input())
    stack, number = preprocess(order, stack)
    if number is not False:
        results.append(number)
    print('스택 변화' , stack)
    print('결과 변화', results)
    
for result in results:
    print(result)