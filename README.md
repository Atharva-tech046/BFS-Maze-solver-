# 🕸️ BFS Maze Pathfinding Visualizer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Library-Pygame-green)
![Algorithm](https://img.shields.io/badge/Algorithm-BFS-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**An interactive graph theory application that generates random mazes and visualizes the Breadth-First Search (BFS) algorithm finding the shortest path in real-time.**

---

## 📖 Project Overview
This project serves as a practical implementation of **Data Structures and Algorithms (DSA)** in Python. It models a 2D grid as an unweighted graph to demonstrate how traversing nodes layer-by-layer guarantees the optimal solution.

### Key Features
* **Real-Time Visualization:** Watch the algorithm scan neighbors, managing the "frontier" of exploration using a Queue.
* **Shortest Path Guarantee:** Implements BFS to ensure the mathematically shortest route is found.
* **Procedural Maze Generation:** Uses the **Recursive Backtracker** algorithm (DFS) to generate infinite, unique, perfect mazes (no loops).
* **Optimized Performance:** Built on `pygame` for smooth rendering and `collections.deque` for $O(1)$ queue operations.

---

## 🛠️ Tech Stack & Libraries
This project relies on standard Python libraries for logic and `pygame` for the interface.

| Library | Type | Purpose in Project |
| :--- | :--- | :--- |
| **`pygame`** | **External** | Handles the GUI, drawing the grid, coloring cells (Visited/Path), and the game loop. |
| **`collections`** | Built-in | Provides **`deque`**, a high-performance Queue (FIFO) essential for BFS efficiency. |
| **`random`** | Built-in | Used to shuffle directions during maze generation so every layout is unique. |
| **`time`** | Built-in | Adds small delays to the visualization so the human eye can track the algorithm's progress. |

---

# 🕸️ BFS Maze Pathfinding Visualizer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Library-Pygame-green)
![Algorithm](https://img.shields.io/badge/Algorithm-BFS-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**An interactive graph theory application that generates random mazes and visualizes the Breadth-First Search (BFS) algorithm finding the shortest path in real-time.**

---

## 📖 Project Overview
This project serves as a practical implementation of **Data Structures and Algorithms (DSA)** in Python. It models a 2D grid as an unweighted graph to demonstrate how traversing nodes layer-by-layer guarantees the optimal solution.

### Key Features
* **Real-Time Visualization:** Watch the algorithm scan neighbors, managing the "frontier" of exploration using a Queue.
* **Shortest Path Guarantee:** Implements BFS to ensure the mathematically shortest route is found.
* **Procedural Maze Generation:** Uses the **Recursive Backtracker** algorithm (DFS) to generate infinite, unique, perfect mazes (no loops).
* **Optimized Performance:** Built on `pygame` for smooth rendering and `collections.deque` for $O(1)$ queue operations.

---

## 🛠️ Tech Stack & Libraries
This project relies on standard Python libraries for logic and `pygame` for the interface.

| Library | Type | Purpose in Project |
| :--- | :--- | :--- |
| **`pygame`** | **External** | Handles the GUI, drawing the grid, coloring cells (Visited/Path), and the game loop. |
| **`collections`** | Built-in | Provides **`deque`**, a high-performance Queue (FIFO) essential for BFS efficiency. |
| **`random`** | Built-in | Used to shuffle directions during maze generation so every layout is unique. |
| **`time`** | Built-in | Adds small delays to the visualization so the human eye can track the algorithm's progress. |

---

## 🧠 Algorithmic Theory
This project is built on three core Computer Science concepts:

### 1. The Graph Model
To the computer, the maze is a **Graph**:
* **Nodes ($V$):** Each cell in the grid.
* **Edges ($E$):** The connections between open cells (Up, Down, Left, Right).
* **Goal:** Traverse from Node A (Start) to Node B (End) with minimum edges.

### 2. Breadth-First Search (BFS)
* **Logic:** BFS moves like a ripple in water. It explores all neighbors 1 step away, then all neighbors 2 steps away, etc.
* **Data Structure:** Uses a **Queue (FIFO - First In, First Out)**. We `enqueue` neighbors and `dequeue` the current cell.
* **Why BFS?** Unlike Depth-First Search (DFS), BFS is **guaranteed** to find the shortest path in an unweighted grid.

### 3. Complexity Analysis
* **Time Complexity:** **$O(V + E)$**
    * In the worst case, the algorithm visits every vertex ($V$) and checks every edge ($E$) exactly once.
* **Space Complexity:** **$O(V)$**
    * To store the `visited` set and the `queue`.

---

## 🚀 Installation & Usage

### Prerequisites
* Python 3.x installed on your system.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/your-username/bfs-maze-solver.git](https://github.com/your-username/bfs-maze-solver.git)
cd bfs-maze-solver
