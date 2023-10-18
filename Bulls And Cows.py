def getHint(secret, guess):
    bulls = 0  # Initialize the count of bulls to 0
    cows = 0  # Initialize the count of cows to 0
    secret_count = {}  # Create an empty dictionary to store the count of each digit in the secret string
    guess_count = {}  # Create an empty dictionary to store the count of each digit in the guess string

    for i in range(len(secret)):
        if secret[i] == guess[i]:  # If the digits at the same index in secret and guess are the same
            bulls += 1  # Increment the count of bulls
        else:
            secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1  # Increment the count of the digit in secret
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1  # Increment the count of the digit in guess

    for key in secret_count:
        if key in guess_count:  # If the digit is present in both secret and guess
            cows += min(secret_count[key], guess_count[key])  # Increment the count of cows by the minimum of the counts for that digit

    return f"{bulls}A{cows}B"  # Return the result in the format "xAyB", where x is the number of bulls and y is the number of cows