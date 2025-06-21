d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}


#Method1 - Pipe operator
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

#Method2 - Using dict.update()

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

d1.update(d2)
print(d1)  # {'a': 1, 'b': 3, 'c': 4}

