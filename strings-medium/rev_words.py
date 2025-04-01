def rev_words(s):
    return " ".join(s.split()[::-1])

sol = rev_words('the sky is blue')
print(sol)