def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()  # Split the string into a list of words
    if len(pattern) != len(words):  # Check if the pattern length matches the number of words
        return False
    
    char_to_word = {}  # Dictionary to store the mapping from characters to words
    word_to_char = {}  # Dictionary to store the mapping from words to characters
    
    for char, word in zip(pattern, words):  # Iterate through each character and word
        if char in char_to_word:  # If the character is already mapped to a word
            if char_to_word[char] != word:  # Check if the mapping is consistent
                return False
        else:
            char_to_word[char] = word  # Add the mapping from character to word
        
        if word in word_to_char:  # If the word is already mapped to a character
            if word_to_char[word] != char:  # Check if the mapping is consistent
                return False
        else:
            word_to_char[word] = char  # Add the mapping from word to character
    
    return True  # If all mappings are consistent, return True