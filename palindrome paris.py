def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    word_indices = {word: i for i, word in enumerate(words)}
    pairs = []

    for i, word in enumerate(words):
        for j in range(len(word) + 1):
            prefix = word[:j]
            suffix = word[j:]

            if is_palindrome(prefix) and suffix[::-1] in word_indices and word_indices[suffix[::-1]] != i:
                pairs.append([i, word_indices[suffix[::-1]]])

            if j != len(word) and is_palindrome(suffix) and prefix[::-1] in word_indices and word_indices[prefix[::-1]] != i:
                pairs.append([word_indices[prefix[::-1]], i])

    return pairs
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(palindrome_pairs(words))