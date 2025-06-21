from collections import defaultdict

def group_anagrams(words):
    anagram_map = defaultdict(list)
    
    for word in words:
        # Sort the characters in the word to form the key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
        
    # Return the grouped anagrams as a list of lists
    return list(anagram_map.values())

# Example usage
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_words)
print(output)
