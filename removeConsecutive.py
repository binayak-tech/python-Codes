def removeConsecutiveCharacter(S):
    stack = [S[0]]
    for i in range(1, len(S)):
        if S[i] != stack[-1]: 
            stack.append(S[i])
        
    return "".join(stack)
    
    
print(removeConsecutiveCharacter("aabbaab"))
