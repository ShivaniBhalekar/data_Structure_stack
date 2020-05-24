def insertAtBottom(stack, item): 
	if len(stack)==0: 
		stack.append(item)
	else: 
		temp = stack.pop()
		insertAtBottom(stack, item) 
		stack.append(temp)

def reverse(stack): 
	if not len(stack)==0: 
		temp = stack.pop() 
		reverse(stack) 
		insertAtBottom(stack, temp) 
def prints(stack): 
	for i in range(len(stack)-1, -1, -1): 
		print(stack[i]) 

stack = []
insertAtBottom(stack,1)
insertAtBottom(stack,2)
insertAtBottom(stack,3)
print("Original Stack ") 
prints(stack) 
reverse(stack) 
print("Reversed Stack ") 
prints(stack) 
