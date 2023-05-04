import sys
visited_states = []     
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
total_moves = 70
expanded = 0 
count =0

class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost

def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)

def expand_node(node):
    expanded_nodes = []
    
    temp_state = move_down(node.state)
    temp_node = create_node(temp_state,node,"down",node.depth+1,node.cost+1)
    expanded_nodes.append(temp_node)

    temp_state1 = move_up(node.state)
    temp_node1 = create_node(temp_state1,node,"up",node.depth+1,node.cost+1)
    expanded_nodes.append(temp_node1)

    temp_state2 = move_left(node.state)
    temp_node2 = create_node(temp_state2,node,"left",node.depth+1,node.cost+1)
    expanded_nodes.append(temp_node2)

    temp_state3 = move_right(node.state)
    temp_node3 = create_node(temp_state3,node,"right",node.depth+1,node.cost+1)
    #print("R",temp_node3.state)
    expanded_nodes.append(temp_node3)

    return expanded_nodes

def move_left(state):
    swap = state.copy()
    idx = swap.index(0)  
    if (idx == 0 or idx == 3 or idx == 6):
        return swap
    else:
        swap[idx-1] , swap[idx] = swap[idx] , swap[idx-1]  
        return swap

def move_right(state):
    swap = state.copy()
    idx = swap.index(0)  
    if (idx == 2 or idx == 5 or idx == 8):
        return swap
    else:
        swap[idx+1] , swap[idx] = swap[idx] , swap[idx+1]  


def move_up(state):
    swap = state.copy()
    idx = swap.index(0) 
    if (idx == 0 or idx == 1 or idx == 2):
        return swap
    else:
        swap[idx-3] , swap[idx] = swap[idx] , swap[idx-3]  
        return swap


def move_down(state):
    swap = state.copy()
    idx = swap.index(0) 
    if (idx == 6 or idx == 7 or idx ==8):
        return swap
    else:
        swap[idx+3] , swap[idx] = swap[idx] , swap[idx+3]  
        return swap



def bfs(start, goal):

    if (start == goal):
        return [None]
    else:
        to_be_expanded = []  
        current_node = create_node(start,None,None,0,0)       
        to_be_expanded.append(current_node) 
    
        for i in range(total_moves):
            temp_expanded = []
            size = len(to_be_expanded)         
            for j in range(size) :
                if (to_be_expanded[j] in visited_states) :  
                    continue;
                node_array = expand_node(to_be_expanded[j])
                for x in range(4):
                    if (node_array[x].state == goal):
                        count = i+1
                        print()
                        print("GOAL STATE FOUND!!!",node_array[x].state)
                        print()
                        print("0 | 1 | 2")
                        print("3 | 4 | 5")
                        print("6 | 7 | 8")
                        return node_array[x]                        
                    else :
                        temp_expanded.append(node_array[x]) 
                        visited_states.append(node_array[x].state) 

            to_be_expanded.clear()  
            to_be_expanded = temp_expanded.copy()   
            temp_expanded.clear()   
    
    return None

def main():
    
    method = 'bfs'
    length = 0
    x = 0
    x = x + 1
    board = "1,2,5,3,4,0,6,7,8"
    board_split = board.split(',')
    starting_state = [int(i) for i in board_split]
    print("_________    Printing state _________")
    print(starting_state)
    if (len(starting_state) == 9):
        result = bfs(starting_state, goal_state)
        if result == None:
            print("No solution found")
        elif result == [None]:
            print  ("Start node was the goal!")
        else:
            print()
            print ("Total number of moves needed = ", result.cost)
            path = [];
            path.append(result.state)
            current = result

            flag = True

            while (flag) :
                parent = current.parent
                prev_state = parent.state
                path.append(prev_state)
                current = parent

                if (prev_state == starting_state) :
                    flag = False

            path.reverse()
            print()
            print("Step-wise Sequence of states from start to goal is ")

            for state in path :
                print(state[0] , " | " , state[1], " | ", state[2])
                print(state[3] , " | " , state[4], " | ", state[5])
                print(state[6] , " | " , state[7], " | ", state[8])
                print()
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()