# Assignment 3

Implementations for three AI search and navigation algorithms, progressing from standard graph search to dynamic grid-based pathfinding.

Before running any of the codes, navigate into this folder.
```sh
cd assignment_3
```

## 1. Dijkstra’s Algorithm (India Road Network)
This program finds the shortest path and uniform-cost search between major cities in India. The dataset is retrieved from a csv file.
*(Note: The road distances dataset used was taken from Kaggle.)*

**How to Run:**
```sh
g++ dijkstra.cpp -o dijkstra
./dijkstra
```

**Example Outputs:**
* **Example 1:** `Start: Delhi, Goal: Kanpur` -> Path: Delhi -> Agra -> Kanpur | Total Cost: 520 km
* **Example 2:** `Start: Chennai, Goal: Mumbai` -> Path: Chennai -> Hyderabad -> Mumbai | Total Cost: 1334 km
* **Example 3:** `Start: Hyderabad, Goal: Pune` -> Path: Hyderabad -> Pune | Total Cost: 562 km

---

## 2. Static UGV Navigation (A* Search)
This simulates an Unmanned Ground Vehicle (UGV) finding the optimal path across a 70x70 km battlefield using the A* Search algorithm with an 8-way movement heuristic. The algorithm knows the locations of all obstacles in advance.

**How to Run:**
```sh
g++ ugv_static.cpp -o static
./static
```

**Understanding the Output:**
Because the obstacles are generated randomly using a seed every time the program executes, **your output will change on every single run**. The Measures of Effectiveness (Path Cost, Nodes Expanded, and CPU Time) will fluctuate. On High-Density (45%) runs, the UGV may report "Failure" if completely walled off.

---

## 3. Dynamic UGV Navigation (Replanning A*)
This upgrades the UGV to operate in a "Fog of War" environment. Instead of knowing the whole map, the UGV uses a 5x5 sensor range. If a dynamic, unmapped obstacle suddenly appears in its path, it pauses, updates its internal map, and recalculates a new route on the fly.

**How to Run:**
```sh
g++ ugv_dynamic.cpp -o dynamic
./dynamic
```

**Understanding the Output:**
Similar to the static version, the total number of execution steps will vary on every run based on where and when the dynamic obstacles "appear". If a dynamic wall completely traps the UGV mid-route, it will trigger a localized failure state.

## 4. Question: Dynamic Navigation Strategy

**Q: In a real world, obstacles can be dynamic and not known a priori. How do you make the UGV navigate and find the optimal path in a dynamic obstacles environment?**

**A:** To navigate dynamic, unknown obstacles, the UGV must switch from planning just once to a continuous "sense and react" loop:

1. **Local Sensors:** Equip the UGV with localized sensors (like LiDAR or cameras) to scan a short radius around itself as it moves.
2. **Dual Mapping:** Maintain two maps: a "Global Map" (what it knew at the start) and a "Local Map" (which constantly updates with real-time sensor data).
3. **Dynamic Pathfinding:** Replace standard A* with an algorithm built for changing environments:
    * **Replanning A\*:** If the sensor detects a new obstacle blocking the path, the UGV stops and runs A* again from its current location to the goal. This is simpler to implement but heavier on the CPU.
    * **D\* Lite:** An advanced algorithm that searches backward from the goal. When a new obstacle appears, it only updates the specific grid cells affected by the blockage. This is highly efficient.
