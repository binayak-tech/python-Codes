def parentheses(s):
    hashMap = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    
    # We are using a stack, 
    # insert open parenthesis on the top of the stack, 
    # remove from top of stack if we get correct closing parenthesis
    
    stack = []
    
    for i in s:
        if i in hashMap:
            if stack and stack[-1] == hashMap[i]: 
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    if len(stack) == 0:
        return True
    else: 
        return False
        

print(parentheses("([{}])"))
