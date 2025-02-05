# Given an array of size N. Find the highest and lowest frequency element.
# method 1: using counter
def freq(arr,n):
    mp={}
    h=0
    l=n
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]]+=1
        else:
            mp[arr[i]]=1
    for j in mp:
        if h < mp[j]:
            h=mp[j]
            he = j
        if mp[j] <= l:
            l=mp[j]
            le=j
        print(j,mp[j])
    print("high freq is {} and the element is {}".format(h,he))
    print("low freq is {} and the element is {}".format(l,le))
if __name__ == "__main__":
    arr = [4,4,4,5,5,6,6,6,6,6,6]
    n=len(arr)
    freq(arr,n)

# method 2:  using max and min and lambda functions 
def Frequency(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])
    return mp
    
def find_highest_lowest_frequency(arr, n):
    freq_map = Frequency(arr, n)  # Get the frequency dictionary

    max_freq = max(freq_map.values())  # Find maximum frequency
    min_freq = min(freq_map.values())  # Find minimum frequency

    # Find elements with max and min frequency
    highest_freq_elements = list(filter(lambda x: freq_map[x] == max_freq, freq_map))
    lowest_freq_elements = list(filter(lambda x: freq_map[x] == min_freq, freq_map))

    return highest_freq_elements, lowest_freq_elements

if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    
    highest, lowest = find_highest_lowest_frequency(arr, n)

    print("\nHighest Frequency Elements:", highest)
    print("Lowest Frequency Elements:", lowest)