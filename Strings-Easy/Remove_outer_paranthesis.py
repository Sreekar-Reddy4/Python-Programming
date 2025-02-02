def removeOuterParentheses(s) -> str:
        count = 0
        res=''
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                count-=1
            
            if (count==1 and s[i]=='(' or count==0):
                continue
            else:
                res+=s[i]
        return res

sol = removeOuterParentheses("(()())(())")
print(sol) 

