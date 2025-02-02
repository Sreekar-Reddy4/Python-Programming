def get_elements(arr):
    xor=0
    for i in arr:
        xor^=i
    return xor

arr = [2,2,1]
print(get_elements(arr))