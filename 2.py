import random
def conflicts(board):
    c = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i]-board[j]) == abs(i-j):
                c += 1
    return c
# hill climbing

def hill_climb(board):
    n = len(board)
    
    while True:
        current = conflicts(board)
        if current == 0:
            return board
        
        improved = False
        
        for col in range(n):
            best = board[col]
            min_c = current
            
            for row in range(n):
                board[col] = row
                c = conflicts(board)
                
                if c < min_c:
                    min_c = c
                    best = row
                    improved = True
            
            board[col] = best
        
        if not improved:
            return None

def n_queens(n=8):
    while True:
        board = [random.randint(0, n-1) for _ in range(n)]
        result = hill_climb(board)
        if result:
            return result

print("Solution:", n_queens())

# water Jug

from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    path = []

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

        if x == target or y == target:
            print("Solution Path:")
            for step in path:
                print(step)
            return

        queue.extend([
            (jug1, y),       
            (x, jug2),       
            (0, y),          
            (x, 0),          
            (min(jug1, x+y), max(0, x+y-jug1)),  
            (max(0, x+y-jug2), min(jug2, x+y))   
        ])

    print("No solution")

water_jug(4, 3, 2)

# tower

def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)
towers_of_hanoi(3, 'A', 'B', 'C')