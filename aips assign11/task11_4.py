class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a new node into the Binary Search Tree."""
        if self.root is None:
            self.root = Node(data)
            return
        
        self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        """Helper method to recursively insert a node."""
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self):
        """Perform inorder traversal and display the BST elements."""
        if self.root is None:
            print("BST is empty.")
            return
        
        result = []
        self._inorder_recursive(self.root, result)
        print("Inorder traversal:", " -> ".join(map(str, result)))

    def _inorder_recursive(self, node, result):
        """Helper method to recursively perform inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

if __name__ == "__main__":
    print("=" * 50)
    print("Task Description #4 – Binary Search Tree (BST)")
    print("=" * 50)
    
    bst = BST()
    while True:
        print("\n1. Insert\n2. Inorder traversal\n3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            try:
                data = int(input("Enter data to insert: "))
                bst.insert(data)
                print(f"Inserted {data}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            bst.inorder_traversal()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
