def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

# Get user input
input_string = input("Enter a string: ")

# Call the function to count vowels and consonants
vowel_count, consonant_count = count_vowels_and_consonants(input_string)

# Print the results
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")