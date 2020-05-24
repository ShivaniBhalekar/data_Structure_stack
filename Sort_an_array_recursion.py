def sorting(stack,item):
    if len(stack)==0 or item > stack[-1]:
        stack.append(item)
    else:
        temp=stack.pop()
        sorting(stack,item)
        stack.append(temp)
def sort(stack):
    if len(stack)!=0:
        temp=stack.pop()
        sort(stack)
        sorting(stack,temp)
def printStack(stack):
    for i in stack[::-1]:
        print(i)

stack=[3,6,9,7]
sort(stack)
printStack(stack)
        
    
