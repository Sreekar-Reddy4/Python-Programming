###Sorting ensures that the smallest (first) and largest (last) strings in lexicographic order will have the minimum common prefix shared across all strings in the list.

Key Idea:

Lexicographic sorting arranges words alphabetically (like a dictionary).

Since prefixes are preserved in sorted order, the longest common prefix (LCP) of the entire list is guaranteed to be the LCP of the first and last string.##







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