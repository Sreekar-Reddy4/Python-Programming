 #Input: s = "the sky is blue"
# Output: "blue is sky the"



def reverseWords(s: str) -> str:
        return " ".join(s.split()[::-1])


s = "the sky is blue"

result = reverseWords(s)
print(result)