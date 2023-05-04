import random

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the initial state (randomly shuffled)
initial_state = [[4, 1, 3], [7, 2, 6], [0, 5, 8]]

# Define the heuristic function (number of misplaced tiles)
def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Define the hill climbing algorithm
def hill_climbing(state, heuristic):
    while True:
        neighbors = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    if i > 0:
                        neighbor = [row[:] for row in state]
                        neighbor[i][j], neighbor[i-1][j] = neighbor[i-1][j], neighbor[i][j]
                        neighbors.append(neighbor)
                    if i < 2:
                        neighbor = [row[:] for row in state]
                        neighbor[i][j], neighbor[i+1][j] = neighbor[i+1][j], neighbor[i][j]
                        neighbors.append(neighbor)
                    if j > 0:
                        neighbor = [row[:] for row in state]
                        neighbor[i][j], neighbor[i][j-1] = neighbor[i][j-1], neighbor[i][j]
                        neighbors.append(neighbor)
                    if j < 2:
                        neighbor = [row[:] for row in state]
                        neighbor[i][j], neighbor[i][j+1] = neighbor[i][j+1], neighbor[i][j]
                        neighbors.append(neighbor)
        if not neighbors:
            break
        best_neighbor = min(neighbors, key=heuristic)
        print("visited state:")      
        for row in best_neighbor:
            print(row)
        print("Heusristic value:",heuristic(best_neighbor))
        if heuristic(best_neighbor) >= heuristic(state):
            break
        state = best_neighbor
    return state

# Solve the n-puzzle problem
print("Initial state:")
for row in initial_state:
    print(row)
print("")

final_state = hill_climbing(initial_state, misplaced_tiles)

print("Final state:")
for row in final_state:
    print(row)
print("")
