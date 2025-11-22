class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)
        print(f"Enqueued {item} to queue.")

    def dequeue(self):
        """Remove and return the front item of the queue. Return None if queue is empty."""
        if not self.is_empty():
            dequeued_item = self.items.pop(0)
            print(f"Dequeued {dequeued_item} from queue.")
            return dequeued_item
        print("Queue is empty. Cannot dequeue.")
        return None

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

# Demo: interactively take input from user
if __name__ == "__main__":
    print("=" * 50)
    print("Task Description #2 – Queue Implementation")
    print("=" * 50)
    print("\nThis program implements a Queue class with:")
    print("- enqueue(): Add an item to the back of the queue")
    print("- dequeue(): Remove and return the front item from the queue")
    print("- is_empty(): Check if the queue is empty")
    print("=" * 50)
    
    queue = Queue()
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if empty")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

