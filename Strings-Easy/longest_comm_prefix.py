def longest_common(lst):
    res = ""
    lst = sorted(lst)
    first = lst[0]
    last = lst[-1]
    for i in range(len(first)):
        if first[i] == last[i]:
            res += first[i]
        else:
            break
    return res

sol = longest_common(["flower", "flow", "flight"])
print(sol)  