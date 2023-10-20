class ValidWordAbbr:
    def __init__(self, dictionary):
        self.abbreviations = {}  # Initialize an empty dictionary to store abbreviations
        
        for word in dictionary:
            abbreviation = self.getAbbreviation(word)  # Get the abbreviation for the current word
            if abbreviation not in self.abbreviations:
                # If the abbreviation is not already present in the abbreviations dictionary
                self.abbreviations[abbreviation] = set()  # Create a new set to store words with the same abbreviation
            self.abbreviations[abbreviation].add(word)  # Add the current word to the set of words with the same abbreviation
    
    def getAbbreviation(self, word):
        if len(word) <= 2:
            return word  # If the word length is less than or equal to 2, return the word itself as the abbreviation
        return word[0] + str(len(word) - 2) + word[-1]  # Calculate the abbreviation for the word
    
    def isUnique(self, word):
        abbreviation = self.getAbbreviation(word)  # Get the abbreviation for the given word
        if abbreviation not in self.abbreviations:
            return True  # If the abbreviation is not present in the abbreviations dictionary, the word is unique
        words = self.abbreviations[abbreviation]  # Get the set of words with the same abbreviation
        return len(words) == 1 and word in words  # Return True if the set contains only the given word, indicating uniqueness