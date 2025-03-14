#Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true


def isomorphic_str(s,t):
    if len(s)!=len(t):
        return False
    s1={}
    t1={}
    for i,j in zip(s,t):
        if i in s1 and s1[i]!=j:
            return False
        if j in t1 and t1[j]!=i:
            return False
        s1[i]=j
        t1[j]=i
    return True

s = "egg"
t = "add"
solution = isomorphic_str(s,t)
print(solution)