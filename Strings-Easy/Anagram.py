#Input: s = "anagram", t = "nagaram"

# Output: true


def isAnagram(s,t) -> bool:
        if len(s) != len (t):
            return False
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True

s = 'anagram'
t = 'nagaram'
res = isAnagram(s,t)
print(res)
