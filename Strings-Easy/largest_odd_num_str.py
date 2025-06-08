def largest_odd_num(str):
    n = len(str)
    for i in range(n-1, -1, -1):
        print(i)
        if int(str[i]) % 2 != 0:
            return str[:i+1]
        else:
            return str[1:i+1]
    return ""
sol = largest_odd_num("35427")
print(sol) 



## remove leading zeros
# def largest_odd_number(s):
#     for i in range(len(s)-1, -1, -1):
#         if int(s[i]) % 2 != 0:
#             return s[:i+1].lstrip('0')
#     return ""
