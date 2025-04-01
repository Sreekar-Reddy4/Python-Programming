def rotate_str(s,t):
    if len(s)!=len(t):
        return False
    elif t in (s+s):
        return True
    else:
        return False

s='abcde'
t='bcdea'
result = rotate_str(s,t)
print(result)