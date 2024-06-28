def duplicate_encode(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()

    # Create a dictionary to store character counts
    char_counts = {}

    # Count the occurrences of each character
    for char in word:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Create a new string with the encoded characters
    encoded = ""
    for char in word:
        if char_counts[char] > 1:
            encoded += ")"
        else:
            encoded += "("

    return encoded


# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])