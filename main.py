import pygame
import random
from collections import deque

# --- CONFIGURATION ---
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 40
COLS, ROWS = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
FPS = 60

# --- COLORS ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)      # Visited cells during generation/solving
GREEN = (0, 255, 0)    # Solution Path
BLUE = (0, 0, 255)     # Current head of the solver
DARK_GREY = (40, 40, 40)

# --- INITIALIZE PYGAME ---
pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("BFS Maze Solver - Recursive Backtracker & BFS")

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        
    def draw_current(self, color):
        x, y = self.x * TILE_SIZE, self.y * TILE_SIZE
        pygame.draw.rect(sc, color, (x + 2, y + 2, TILE_SIZE - 2, TILE_SIZE - 2))

    def draw(self):
        x, y = self.x * TILE_SIZE, self.y * TILE_SIZE
        # Draw Walls (Lines)
        if self.walls['top']:
            pygame.draw.line(sc, WHITE, (x, y), (x + TILE_SIZE, y), 2)
        if self.walls['right']:
            pygame.draw.line(sc, WHITE, (x + TILE_SIZE, y), (x + TILE_SIZE, y + TILE_SIZE), 2)
        if self.walls['bottom']:
            pygame.draw.line(sc, WHITE, (x + TILE_SIZE, y + TILE_SIZE), (x, y + TILE_SIZE), 2)
        if self.walls['left']:
            pygame.draw.line(sc, WHITE, (x, y + TILE_SIZE), (x, y), 2)

    def check_neighbors(self, grid_cells):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1, grid_cells)
        right = self.check_cell(self.x + 1, self.y, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, grid_cells)
        left = self.check_cell(self.x - 1, self.y, grid_cells)

        if top and not top.visited: neighbors.append(top)
        if right and not right.visited: neighbors.append(right)
        if bottom and not bottom.visited: neighbors.append(bottom)
        if left and not left.visited: neighbors.append(left)

        return random.choice(neighbors) if neighbors else None

    def check_cell(self, x, y, grid_cells):
        find_index = lambda x, y: x + y * COLS
        if x < 0 or x > COLS - 1 or y < 0 or y > ROWS - 1:
            return None
        return grid_cells[find_index(x, y)]

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

# --- MAZE GENERATION (Recursive Backtracker) ---
def generate_maze():
    grid_cells = [Cell(col, row) for row in range(ROWS) for col in range(COLS)]
    current_cell = grid_cells[0]
    stack = []
    
    while True:
        sc.fill(DARK_GREY)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()

        # Draw all cells
        [cell.draw() for cell in grid_cells]
        current_cell.visited = True
        current_cell.draw_current(RED) # Highlight generator head
        
        next_cell = current_cell.check_neighbors(grid_cells)
        if next_cell:
            next_cell.visited = True
            stack.append(current_cell)
            remove_walls(current_cell, next_cell)
            current_cell = next_cell
        elif stack:
            current_cell = stack.pop()
        else:
            break # Maze generation finished
        
        pygame.display.flip()
        # clock.tick(100) # Uncomment to slow down generation visualization

    return grid_cells

# --- BFS SOLVER ---
def solve_bfs(grid_cells):
    start_cell = grid_cells[0]
    end_cell = grid_cells[-1] # Bottom-right corner
    
    queue = deque([start_cell])
    visited = {start_cell}
    parent_map = {start_cell: None} # To reconstruct path
    path = []
    
    # Helper to find neighbors based on walls
    def get_valid_neighbors(cell):
        neighbors = []
        index = lambda x, y: x + y * COLS
        
        # Check Top
        if not cell.walls['top']:
            n = grid_cells[index(cell.x, cell.y - 1)]
            if n not in visited: neighbors.append(n)
        # Check Right
        if not cell.walls['right']:
            n = grid_cells[index(cell.x + 1, cell.y)]
            if n not in visited: neighbors.append(n)
        # Check Bottom
        if not cell.walls['bottom']:
            n = grid_cells[index(cell.x, cell.y + 1)]
            if n not in visited: neighbors.append(n)
        # Check Left
        if not cell.walls['left']:
            n = grid_cells[index(cell.x - 1, cell.y)]
            if n not in visited: neighbors.append(n)
            
        return neighbors

    solved = False
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: exit()

        current = queue.popleft()
        
        if current == end_cell:
            solved = True
            break # Found the end!

        for neighbor in get_valid_neighbors(current):
            visited.add(neighbor)
            parent_map[neighbor] = current
            queue.append(neighbor)
            
            # Visualization: Draw visited cells (Blue Flood)
            neighbor.draw_current(BLUE)
        
        # Redraw grid lines on top so we can see walls
        [c.draw() for c in grid_cells]
        pygame.display.flip()
        # clock.tick(60) # Control BFS speed

    # Reconstruct Path
    if solved:
        curr = end_cell
        while curr:
            path.append(curr)
            curr = parent_map[curr]
            
            # Draw final path
            path_node = path[-1]
            path_node.draw_current(GREEN)
            [c.draw() for c in grid_cells]
            pygame.display.flip()
            clock.tick(20) # Animation speed for path drawing

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("Generating Maze...")
    maze = generate_maze()
    print("Maze Generated! Starting BFS Solver...")
    solve_bfs(maze)
    print("Solved! Close window to exit.")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()