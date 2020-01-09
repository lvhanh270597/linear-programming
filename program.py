# import the library pulp as p 
import pulp as p 

# Create a LP Minimization problem 
# Lp_prob = p.LpProblem('Problem', p.LpMinimize) 
Lp_prob = p.LpProblem('Problem', p.LpMaximize) 

# Create problem Variables 
x = p.LpVariable("x", lowBound = 0) # Create a variable x >= 0 
y = p.LpVariable("y", lowBound = 0) # Create a variable y >= 0 

# Objective Function 
Lp_prob += 8 * x + 6 * y

# Constraints: 
Lp_prob += 4 * x + 2 * y <= 60
Lp_prob += 2 * x + 4 * y <= 48

# Display the problem 
print(Lp_prob) 

status = Lp_prob.solve() # Solver 
print(p.LpStatus[status]) # The solution status 

# Printing the final solution 
print("x = %f, y = %f, optimal: %f" % (p.value(x), p.value(y), p.value(Lp_prob.objective)))
