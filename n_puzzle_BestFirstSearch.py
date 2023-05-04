
# from queue import PriorityQueue
# from queue import Queue
# from queue import LifoQueue
    
# def Greedy(given_state , n):
#     frontier = PriorityQueue()
#     explored = []
#     counter = 0
#     root = State(given_state, None, None, 0, 0)
#     #root.evaluation()
#     evaluation = root.Misplaced_Tiles(n) #we can use Misplaced_Tiles() instead.
#     frontier.put((evaluation, counter, root)) #based on greedy evaluation
#     while not frontier.empty():
       
#         current_node = frontier.get()
#         current_node = current_node[2]
#         explored.append(current_node.state)
#         # print("current node:")
#         # print(*current_node.state)
#         # print("hueristic value of current node:-", evaluation)
#         if current_node.test():
#             return current_node.solution(), len(explored)

#         children = current_node.expand(n)
#         for child in children:
#             if child.state not in explored:
#                 counter += 1
#                 evaluation = child.Misplaced_Tiles(n) #we can use Misplaced_Tiles() instead.
                
#                 frontier.put((evaluation, counter, child)) #based on greedy evaluation
#     return


# class State:
#     goal = [1, 2, 3, 4,5,6,7,8,0] 
    
#     greedy_evaluation = None
#     heuristic = None
#     def __init__(self, state, parent, direction, depth, cost):
#         self.state = state
#         self.parent = parent
#         self.direction = direction
#         self.depth = depth

#         if parent:
#             self.cost = parent.cost + cost

#         else:
#             self.cost = cost

            
            
#     def test(self): #check if the given state is goal
#         if self.state == self.goal:
#             return True
#         return False


#     #heuristic function based on number of misplaced tiles
#     def Misplaced_Tiles(self,n): 
#         counter = 0;
#         for i in range(n*n):
#                 if (self.state[i] != self.goal[i]):
#                     counter += 1
#                 self.heuristic = counter
#         self.greedy_evaluation = self.heuristic    

#         return( self.greedy_evaluation)                
                    


#     @staticmethod
    
#     #this would remove illegal moves for a given state
#     def available_moves(x,n): 
#         moves = ['Left', 'Right', 'Up', 'Down']
#         if x % n == 0:
#             moves.remove('Left')
#         if x % n == n-1:
#             moves.remove('Right')
#         if x - n < 0:
#             moves.remove('Up')
#         if x + n > n*n - 1:
#             moves.remove('Down')

#         return moves

#     #produces children of a given state
#     def expand(self , n): 
#         x = self.state.index(0)
#         moves = self.available_moves(x,n)
        
#         children = []
#         for direction in moves:
#             temp = self.state.copy()
#             if direction == 'Left':
#                 temp[x], temp[x - 1] = temp[x - 1], temp[x]
#             elif direction == 'Right':
#                 temp[x], temp[x + 1] = temp[x + 1], temp[x]
#             elif direction == 'Up':
#                 temp[x], temp[x - n] = temp[x - n], temp[x]
#             elif direction == 'Down':
#                 temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
#             children.append(State(temp, self, direction, self.depth + 1, 1)) #depth should be changed as children are produced
#         return children

    
#     #gets the given state and returns it's direction + it's parent's direction till there is no parent
#     def solution(self):
#         solution = []
#         solution.append(self.direction)
#         path = self
#         print("visited State.                 hueristic Value")
#         while path.parent != None:
            
#             path = path.parent
#             print(path.state ,"        ", path.Misplaced_Tiles(n))
             
#             solution.append(path.direction)
#         solution = solution[:-1]
#         solution.reverse()
#         return solution

# #initial state
# n=3
# root=[5,6,7,4,0,8,3,2,1]





    
# Greedy_solution = Greedy(root, n)
# print('Greedy Solution is ', Greedy_solution[0])
# print('Number of explored nodes is ', Greedy_solution[1])   
    
    
import heapq

def get_misplaced_tile(start , goal):
    counter = 0;
    for i in range(3):
        for j in range(3):
            if (start[i][j] != goal[i][j]):
                counter += 1
    return counter
        
def get_neighbours(puzzle):
    neighbours =[]
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                if i>0:
                    neighbour = [list(row) for row in puzzle]
                    neighbour[i][j],neighbour[i-1][j]=neighbour[i-1][j],  neighbour[i][j]
                    neighbours.append(neighbour)
                if i<2:
                    neighbour = [list(row) for row in puzzle]
                    neighbour[i][j],neighbour[i+1][j]=neighbour[i+1][j],  neighbour[i][j]
                    neighbours.append(neighbour)
                if j>0:
                    neighbour = [list(row) for row in puzzle]
                    neighbour[i][j],neighbour[i][j-1]=neighbour[i][j-1],  neighbour[i][j]
                    neighbours.append(neighbour)
                if j<2:
                    neighbour = [list(row) for row in puzzle]
                    neighbour[i][j],neighbour[i][j+1]=neighbour[i][j+1],  neighbour[i][j]
                    neighbours.append(neighbour)
    return neighbours

def best_first_search(start,goal):
    queue = []
    heapq.heappush(queue,(get_misplaced_tile(start,goal),start))
    cost ={str(start):0}
    parent ={str(start):None}
    visited =set()
    counter_node = 0
    while queue:
        current = heapq.heappop(queue)[1]
        print("Current Puzzle state is: ",current)
        print("Hueristic value of current state: ",get_misplaced_tile(current,goal))
        if current == goal:
            print("Goal State reached")
            solution = [current]
            while parent[str(current)] != None:
                current = parent[str(current)]
                solution.append(current)
            return solution[::-1]
        visited.add(str(current))
        neighbours = get_neighbours(current)
        for neighbour in neighbours:
            if str(neighbour) not in visited:
                counter_node+=1
                heapq.heappush(queue,(get_misplaced_tile(neighbour,goal),neighbour))
            cost[str(neighbour)]=cost[str(current)] + 1
            parent[str(neighbour)]=current
    return True

start = [[0,2,3],[1,4,5],[7,8,6]]
goal = [[1,2,3],[4,5,6],[7,8,0]]
print("Solving the problem we used misplaced distance as our heristic function for best first search.")
print("The starting state is: ",start )
print("The Goal State is: ",goal)
solution = best_first_search(start,goal)


     
         
