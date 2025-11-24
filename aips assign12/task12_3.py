from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the optimization problem
model = LpProblem("Chocolate_Profit_Maximization", LpMaximize)

# Define decision variables
x = LpVariable("Chocolate_A", lowBound=0, cat='Integer')
y = LpVariable("Chocolate_B", lowBound=0, cat='Integer')

# Gather user input for resource availability
milk_available = int(input("Enter available milk units (default 5): ") or 5)
choco_available = int(input("Enter available chocolate units (default 12): ") or 12)

# Add constraints
model += x + y <= milk_available          # Milk constraint
model += 3*x + 2*y <= choco_available     # Choco constraint

# Define objective function
model += 6*x + 5*y           # Profit function

# Solve the problem
model.solve()

# Output results
print("Optimal Production Plan:")
print(f"Produce {int(x.value())} units of Chocolate A")
print(f"Produce {int(y.value())} units of Chocolate B")
print(f"Maximum Profit: Rs {int(value(model.objective))}")