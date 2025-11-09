def count_vowels(text):
    """
    Counts the number of vowels in a given string and returns the vowels found.
    
    Args:
        text (str): The input string to analyze
        
    Returns:
        tuple: A tuple containing (vowels_list, count)
    """
    vowels = 'aeiouAEIOU'
    vowels_found = []
    
    for char in text:
        if char in vowels:
            vowels_found.append(char)
    
    return vowels_found, len(vowels_found)


def main():
    # Take input from user
    user_input = input("Enter a string: ")
    
    # Count vowels and get the list of vowels found
    vowels_list, vowel_count = count_vowels(user_input)
    
    # Print the vowels found
    print(f"\nVowels found: {', '.join(vowels_list) if vowels_list else 'None'}")
    print(f"Number of vowels: {vowel_count}")


if __name__ == "__main__":
    main()

