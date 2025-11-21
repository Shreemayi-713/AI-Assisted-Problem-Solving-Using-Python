def find_common(a, b):
    return list(set(a) & set(b))

# --- User Input Section ---
list1 = input("Enter elements of first list separated by spaces: ").split()
list2 = input("Enter elements of second list separated by spaces: ").split()

common = find_common(list1, list2)
print("Common elements:", common)
