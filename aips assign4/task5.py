def count_lines(filename):
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0


def main():
    # Take input from user
    filename = input("Enter the path to the .txt file: ")
    
    # Count lines in the file
    line_count = count_lines(filename)
    
    # Print the result
    if line_count > 0:
        print(f"\nNumber of lines in '{filename}': {line_count}")
    else:
        print(f"\nCould not count lines in '{filename}'.")




if __name__ == "__main__":
    main()

