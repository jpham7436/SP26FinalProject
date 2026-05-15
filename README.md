# The Torchbearer

**Student Name:** Jason Pham
**Student ID:** 132526911
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
    - A single shortest-path run from S is not enough because finding this tells us nothing about what order we should collect the relics in.

- **What decision remains after all inter-location costs are known:**
    - The decision that remains is choosing the optimal order to retrieve all the relics and reach the exit.

- **Why this requires a search over orders (one sentence):**
    - This requires a search over orders because different permutations of orders can have different fuel costs, so all viable orders must be checked to find the minimum.

---




## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Starting node | Route starts here, so need cost from start to all potential relics |
| All Relic nodes | After choosing a relic, we need costs to choose the next relic or the exit |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | nested dictionary |
| What the keys represent | Outer keys represent source nodes, inner keys represent destination nodes |
| What the values represent | Shortest fuel path discovered so far from the source node to the destinatio node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Because we are using a python dictionary, which has an average O(1) lookup complexity |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** 1 (source node) + k (number of relics) = 1 + k
- **Cost per run:** O(m log n) given by ASSIGNMENT.md
- **Total complexity:** # of runs * cost per run = (k + 1) * O(m log n) = O(k * m log n + m log n) = simplifies to O (k * m log n)
- **Justification (one line):** We run Dijkstra's for every relic node + the starting node, hence k + 1. Cost per run is given by the assignment, so total complexity is # of runs * cost per run.

---




## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
    - Stored distanced have been finalized and will never improve. Dijkstra's has already found the shortest path from source to those nodes.

- **For nodes not yet finalized (not in S):**
    - Stored distance is the shortest path found SO FAR using only finalized nodes as steps. This distance could improve as more nodes are finalized. 

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
    - Source starts with distance 0 b/c no distance from source to source. All other nodes are set to infinity because no paths have been discovered so far.

- **Maintenance : why finalizing the min-dist node is always correct:**
    - All edge weights = nonnegative, so unfinalized node with the smallest distance is already at it's shortest route. Distance can't be improved later by some other unfinalized node.

- **Termination : what the invariant guarantees when the algorithm ends:**
    - The shortest distance to every reachable node from the source has been calculated. Unreachable nodes remain at infinity (because they can never be reached).

### Part 3c: Why This Matters for the Route Planner

Correct distances are important because the Torchbearer will need that information to calculate fuel costs between nodes of interest when comparing different relic orders.

---




## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** - Greedy choices pick relics without considering how the choice affects the remaining choices and cost. For example, greedy may choose the closest relic first
- **Counter-example setup:** - S -> B costs 1, S -> C costs 3, B <-> C costs 1, B -> T costs 1, C -> T costs 10 
- **What greedy picks:** - S -> B (1) -> C (1) -> T (10) -> total: 12
- **What optimal picks:** - S -> C(3) -> B (1) -> T (1) -> total: 5
- **Why greedy loses:** - A locally optimal decision can close off routes for a global optimal solution by putting the Torchbearer in a bad position.

### What the Algorithm Must Explore

- The algorithm must explore the different possible orders to get relics because the final order is what deteremines total fuel cost. 

---




## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | stores exactly where the Torchbearer currently is |
| Relics already collected | relics_remaining | set | stores relics that still need to be collected, collected relics are removed from this list |
| Fuel cost so far | cost_so_far | float | stores total fuel used so far |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Sets average at O(1) for looking up, adding, and removing elements, making it fast|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** k!
- **Why:** With k relics, the algorithm may have to check all possible permutations of the relics, which is k!

---




## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** - The best fuel cost found so far and the order that get that fuel cost
- **When it is used:** - It is checked at the beginning of the function to see if the current cost is >= the best cost
- **What it allows the algorithm to skip:** - It skips any branch whose cost_so_far is already >= the best route found so far because any more paths taken will increase cost_so_far.

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** - Current location, relics still remaining, relic orer so far, and fuel cost so far.
- **What the lower bound accounts for:** - Accounts for fuel that ahs already been spent.
- **Why it never overestimates:** - Because any complete route from this point on must cost at least as much as the fuel already spent

### Part 6c: Pruning Correctness

- If cost_so_far is already >= the best solution, continuing that branch means we will be increasing cost_so_far, making it > the best solution (so we already know that we can prune it out).
- It is important to note that all weights are nonnegative, so adding more paths to the solution will always increase fuel cost.

---


## References

- None beyond lecture notes and recordings (ty for recording lectures btw)
