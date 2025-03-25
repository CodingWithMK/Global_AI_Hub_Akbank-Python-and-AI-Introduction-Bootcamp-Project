# Metro Simulation Project

## 🌐 Project Title and Description
This project simulates a metro network system using Python. It allows users to find the optimal routes between metro stations with two objectives:
1. Find the path with the **least number of transfers** using the **Breadth-First Search (BFS)** algorithm.
2. Find the **fastest path (minimum travel time)** using the **A* (A-Star)** search algorithm.

The metro map includes multiple lines and allows transfer between them at certain stations. The goal is to mimic a real-world public transportation planner.

---

## ⚙️ Technologies and Libraries Used

### Python Standard Libraries
- **`collections`**:
  - `deque`: Used in BFS and A* for queue management (FIFO behavior).
  - `defaultdict`: For storing lines and their corresponding stations.
- **`heapq`**:
  - Used to implement a **priority queue** for A* algorithm. It helps retrieve the node with the smallest `f = g + h` value efficiently.
- **`typing`**:
  - Provides type hinting for better readability and maintenance.

---

## ⚖️ Algorithm Logic and Justification

### ✈️ BFS Algorithm (Breadth-First Search)
- **Purpose**: To find the route between two stations with the **minimum number of line transfers**, regardless of time.
- **How it works**:
  - Uses a **queue (FIFO)** to explore stations level by level.
  - Keeps a **visited set** to avoid revisiting nodes.
  - Stops when destination is reached and returns the path taken.
- **Why we use it**:
  - BFS guarantees the shortest path in terms of **number of edges**, which in our case translates to **minimum transfers**.

### ✨ A* Search Algorithm
- **Purpose**: To find the **fastest route** between two stations, based on actual travel time.
- **How it works**:
  - Combines the actual travel cost (`g`) and a heuristic estimate (`h`) to reach the destination.
  - Uses a **min-heap priority queue** to always expand the station with the lowest `f = g + h`.
  - The heuristic (`h`) is calculated using a **BFS-based estimated time** from the current station to the destination.
- **Why we use it**:
  - A* is more efficient than Dijkstra when a good heuristic is available. It reduces unnecessary exploration and finds the optimal path faster.

---

## 🔢 Example Usage and Test Output

### Scenario 1: From AŞTİ to OSB
```
Route with least transfers:  AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
Fastest route (25 minutes):  AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
```

### Scenario 2: From Batıkent to Keçiören
```
Route with least transfers:  Batıkent -> Demetevler -> Gar -> Keçiören
Fastest route (21 minutes):  Batıkent -> Demetevler -> Gar -> Keçiören
```

### Scenario 3: From Keçiören to AŞTİ
```
Route with least transfers:  Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
Fastest route (19 minutes):  Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
```

---

## 🚫 Notable Challenges and Fixes

### Issue 1: A* returns no result for certain paths
- **Cause**: `calculate_heuristic` was returning `float('inf')` when stations were on different lines.
- **Fix**: Replaced the heuristic function with a **BFS-based shortest time estimation** between stations.

### Issue 2: Infinite loop / 100% RAM usage
- **Cause**: Stations were added to the priority queue multiple times due to missing `visited` checks before `heappush()`.
- **Fix**: Added a `visited.add(neighbor)` line **before** pushing to the heap to avoid revisiting.

### Issue 3: TypeError with heapq
- **Cause**: Python couldn't compare `Station` objects.
- **Fix**: Implemented `__lt__()` method inside `Station` class.

---

## 🚀 Ideas for Future Improvements
- Add a **graphical user interface (GUI)** to visualize the metro map and highlight routes.
- Allow users to **add/remove stations or connections** dynamically.
- Introduce real-time features like **train delays or service closures**.
- Support for **multi-criteria optimization** (e.g., time + transfers).

---

## ✨ Credits
Developed as part of the **Global AI Hub Python & AI Bootcamp (March 2025)** by Muhammed Musab Kaya with the guidance of project mentors and the help of ChatGPT.

---

Thanks for reading and happy coding! 🚀

