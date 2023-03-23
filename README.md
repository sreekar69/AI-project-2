# AI-project-2
Problem statement-
Graph Colouring -You are given a graph in the form of a text file, that you are supposed to colour. The proper vertex colouring is such that each vertex is assigned a colour and no two adjacent vertices are assigned the same colour.
Approach description-
•	Parse the input file to obtain the graph, number of colours, and variables.
•	Define the domains for each variable, initially all colours are allowed for all variables.
•	Define the constraints: adjacent vertices cannot have the same colour.
•	Define the search algorithm: 
a. Check if all variables have been assigned a value. 
b. Select an unassigned variable, using the minimum remaining values heuristic. 
c. Iterate over the domain values of the variable, using the least constraining value heuristic. 
d. Check if the value is consistent with the current assignment and constraints.
 e. Make the assignment and propagate constraints. 
f. If the inference is not a failure, recursively search for a solution. 
g. If the search fails, undo the assignment and revert the domain changes.
•	Define the AC3 algorithm for constraint propagation: a. Initialize the queue with all arcs in the constraints. b. Iterate over the arcs in the queue, and revise the domain of the first variable. c. If the domain of the first variable has been reduced, add all arcs from the first variable to the queue. d. If the domain of any variable is empty, the CSP has no solution.
•	Define helper functions to count conflicts and check consistency.
•	The algorithm uses heuristics to select the next variable and value to assign, in order to reduce the search space and find a solution more efficiently. The minimum remaining values heuristic selects the variable with the fewest remaining values in its domain, while the least constraining value heuristic selects the value that rules out the fewest values in other variables' domains. The AC3 algorithm propagates constraints by iteratively reducing the domains of variables that violate constraints, until a fixed point is reached. The algorithm uses backtracking search to recover from failed assignments and continue the search for a solution.




#How to implement
Run from the terminal----python main.py "C:\Users\sreek\PycharmProjects\AI project 2\input"
