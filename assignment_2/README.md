# Assignment 2

## Searches
This directory contains basic C++ demonstrations of Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's algorithm. Additionally, it includes implementations that solve the classic Missionary and Cannibal river-crossing puzzle using both DFS and BFS to find a valid sequence of moves.

**Example Input/Output (BFS):**
For a simple graph with 4 vertices and 4 edges (a square: 0-1, 0-2, 1-3, 2-3):
```text
Enter the number of vertices and edges: 4 4
Enter the edges: 
0 1
0 2
1 3
2 3
0 1 2 3 
```

**Example Input/Output (DFS):**
Using the same simple graph with 4 vertices and 4 edges:
```text
Enter the number of vertices and edges: 4 4
Enter the edges: 
0 1
0 2
1 3
2 3
0 1 3 2 
```

**Example Input/Output (Dijkstra):**
For a weighted graph with 4 vertices and 4 edges:
```text
Enter the number of vertices and edges: 4 4
Enter the edges (u v weight): 
0 1 2
0 2 4
1 2 1
2 3 3
Enter source vertex: 0
0 2 3 6 
```

## Captcha
This is a simple web-based CAPTCHA application that asks users to solve a basic math problem (addition or subtraction) to prove they are human. The application dynamically generates an image containing the math question overlaid with visual noise (random lines) to deter automated bots. It securely verifies the user's submitted answer and ensures that each CAPTCHA session expires after a single use.

**Installation & Execution:**
This program requires Python, Flask, and Pillow. 

1. Install the required dependencies using pip:
   ```bash
   pip install Flask Pillow
   ```
2. Run the application:
   ```bash
   python run.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000` to view and interact with the CAPTCHA.

## AQI
The AQI (Air Quality Index) project is maintained as a separate repository and is included in this directory as a Git submodule. Please navigate to the AQI project folder and refer to its own dedicated `README.md` for complete details, documentation, and setup instructions.
