''' LIFO -  last in first out
        or
    FILO - First in last out

'''

# Operations
# push - add elements
# Pop - remove elements

# Push operation
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# pop operation
stack.pop()
print(stack)
stack.pop()
print(stack)

stack1 = []
print(len(stack1)==0)
stack1.append(10)
stack1.append(20)
print(stack1[-1])



