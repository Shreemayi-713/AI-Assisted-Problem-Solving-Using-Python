def count_vowels(text):
 
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


def main():
    # Take input from user
    user_input = input("Enter a string: ")
    
    # Count vowels
    vowel_count = count_vowels(user_input)
    
    # Print in the format: Word – X Vowels
    print(f"{user_input} – {vowel_count} Vowels")


if __name__ == "__main__":
    main()

