# ShoppingCart Class Definition
class ShoppingCart:
    def __init__(self):
        self.items = {}  # {name: price}

    def add_item(self, name, price):
        """Add an item with its price"""
        self.items[name] = price
        print(f"Added {name} for ₹{price}")

    def remove_item(self, name):
        """Remove an item if it exists"""
        if name in self.items:
            del self.items[name]
            print(f"Removed {name}")
        else:
            print(f"Item '{name}' not found in cart")

    def total_cost(self):
        """Calculate total price"""
        return sum(self.items.values())
# Test Cases for ShoppingCart Methods
def run_tests():
    print("\n--- Running Test Cases ---")
    
    cart = ShoppingCart()
    
    # Test 1: Add items
    cart.add_item("Apples", 50)
    cart.add_item("Milk", 30)
    assert cart.total_cost() == 80, "Test 1 Failed: Incorrect total after adding items"

    # Test 2: Remove existing item
    cart.remove_item("Milk")
    assert cart.total_cost() == 50, "Test 2 Failed: Incorrect total after removal"

    # Test 3: Remove non-existing item
    cart.remove_item("Bread")  # Should show 'not found' message

    # Test 4: Add another item
    cart.add_item("Eggs", 60)
    assert cart.total_cost() == 110, "Test 4 Failed: Total not updated correctly"

    print("All tests passed successfully!")


# --------------------------
# User Input Functionality
# --------------------------

def user_input_demo():
    print("\n--- Shopping Cart (User Input Mode) ---")
    cart = ShoppingCart()
    
    while True:
        print("\nChoose an option:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View total cost")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            cart.add_item(name, price)

        elif choice == "2":
            name = input("Enter item name to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            print(f"Total cost = ₹{cart.total_cost()}")

        elif choice == "4":
            print("Exiting Shopping Cart...")
            break

        else:
            print("Invalid choice, try again!")

# --------------------------
# Run Test Cases + User Mode
# --------------------------

if __name__ == "__main__":
    run_tests()          # Auto test cases
    user_input_demo()    # User interaction



