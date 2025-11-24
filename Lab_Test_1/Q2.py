class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def delete_value(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev, curr = curr, curr.next
        return False

    def __str__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        return " -> ".join(nodes) if nodes else "Empty"

if __name__ == "__main__":
    ll = SinglyLinkedList()
    print("Enter commands: insert <value>, delete <value>, show, quit")
    while True:
        try:
            parts = input(">> ").strip().split()
        except EOFError:
            print("\nInput stream closed. Exiting.")
            break
        if not parts:
            continue
        cmd = parts[0].lower()
        if cmd == "insert" and len(parts) == 2:
            try:
                ll.insert_end(int(parts[1]))
            except ValueError:
                print("Please provide an integer value.")
        elif cmd == "delete" and len(parts) == 2:
            try:
                value = int(parts[1])
            except ValueError:
                print("Please provide an integer value.")
                continue
            if not ll.delete_value(value):
                print("Value not found")
        elif cmd == "show":
            print(ll)
        elif cmd == "quit":
            break
        else:
            print("Invalid command")