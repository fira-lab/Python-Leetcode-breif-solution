def lengthOfLongestSubstring(s):
    # Create an empty hash map
    hashmap = {}
    # Initialize variables
    start = 0
    max_length = 0
    # Iterate through the string
    for end in range(len(s)):
        # Check if the current character is already in the hash map
        if s[end] in hashmap:
            # Update the start pointer to the next index after the last occurrence of the current character
            start = max(start, hashmap[s[end]] + 1)
        # Update the last occurrence of the current character in the hash map
        hashmap[s[end]] = end
        # Update the maximum length
        max_length = max(max_length, end - start + 1)
    # Return the maximum length
    return max_length