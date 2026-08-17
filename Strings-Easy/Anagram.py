
#brute force

str1 = 'RULES' 
str2 = 'LESRT'
flag = True
if len(str1)!=len(str2):
    print(False)

str1 = sorted(str1)
str2 = sorted(str2)
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        flag = False
print(flag)


#optimal

def check_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    freq = [0] * 26  # Only 26 English letters, constant space

    for ch1, ch2 in zip(str1, str2):
        if ch1.isalpha():
            freq[ord(ch1.lower()) - ord('a')] += 1
        if ch2.isalpha():
            freq[ord(ch2.lower()) - ord('a')] -= 1

    # If all frequencies are zero, it's an anagram
    return all(count == 0 for count in freq)

# ✅ Examples
print(check_anagrams("CaT", "tAc")) 
print(check_anagrams("Hello", "Olelh"))   # True
print(check_anagrams("Listen", "Silent")) # True
print(check_anagrams("Test", "Taste"))    # False



s2 = 'hello'
s1 = 'helloo'
flag = True
d = {}

for i in range(len(s1)):
    if s1[i] not in d:
        d[s1[i]]=1
    else:
        d[s1[i]]+=1

for j in range(len(s2)):
    if s2[j] in d:
        d[s2[j]]-=1
        
for k in range(len(s1)):
    if s1[k] in d and d[s1[k]]==0:
        flag=True
    else:
        flag=False
        break
print(flag)