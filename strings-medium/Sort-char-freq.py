def sort_char(str):
    from collections import Counter
    freq=Counter(str)
    sorted_char = sorted(freq.keys(), key=lambda x: -freq[x])
    return ''.join(i*freq[i] for i in sorted_char)

result = sort_char('tree')
print(result)