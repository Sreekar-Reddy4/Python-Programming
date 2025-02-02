def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
            
        elif c == '{':
            stack.append('}')
            
        elif c == '[':
            stack.append(']')
            
        elif not stack or stack.pop() != c:
            return False
                
    return not stack
        
sol = is_valid("()[]{}")
print(sol)