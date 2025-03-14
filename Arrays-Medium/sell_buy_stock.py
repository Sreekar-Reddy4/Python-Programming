#prices = [7,1,5,3,6,4]
# Output:
#  5
# Explanation:
#  Buy on day 2 (price = 1) and 
# sell on day 5 (price = 6), profit = 6-1 = 5.

#brute force 
def sell_buy_stock(arr):
    max_profit = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                max_profit = max(max_profit,arr[j]-arr[i])
    return max_profit

arr = [7,1,5,3,6,4]
sol = sell_buy_stock(arr)
# print(sol)


#optimal
def buy_sell_opt(arr):
    max_profit = 0
    min_ele = float('inf')
    for i in range(len(arr)):
        min_ele = min(min_ele,arr[i])
        max_profit = max(max_profit,arr[i]-min_ele)
    return max_profit

ans = buy_sell_opt([7,1,5,6,3,4])
print(ans)
    