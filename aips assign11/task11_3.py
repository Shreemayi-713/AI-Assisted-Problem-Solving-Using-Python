class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning of the linked list.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end of the linked list.")
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end of the linked list.")

    def display(self):
        """Display all elements in the linked list."""
        if self.head is None:
            print("Linked list is empty.")
            return
        
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print("Linked list:", " -> ".join(elements))


# Demo: interactively take input from user
if __name__ == "__main__":
    print("=" * 50)
    print("Task Description #3 – Linked List Implementation")
    print("=" * 50)
    print("\nThis program implements a singly linked list with:")
    print("- insert_at_end(): Insert a node at the end of the linked list")
    print("- insert_at_beginning(): Insert a node at the beginning of the linked list")
    print("- display(): Display all elements in the linked list")
    print("=" * 50)
    
    linked_list = LinkedList()
    while True:
        print("\nChoose an operation:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Display linked list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = input("Enter data to insert at beginning: ")
            linked_list.insert_at_beginning(data)
        elif choice == '2':
            data = input("Enter data to insert at end: ")
            linked_list.insert_at_end(data)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

