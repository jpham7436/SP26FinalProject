"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Jason Pham
Student ID:   132526911

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """
    answer = (
        "- A single shortest-path run from S is not enough because finding this tells us nothing about what order we should collect the relics in.\n"
        "- The decision that remains is choosing the optimal order to retrieve all the relics and reach the exit.\n"
        "- This requires a search over orders because different permutations of orders can have different fuel costs, so all viable orders must be checked to find the minimum.\n"
    )
    return answer


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    sources = [spawn]

    for relic in relics:
        sources.append(relic)
    
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    """
    dist = {}

    # Set all distances to inf
    for node in graph:
        dist[node] = float('inf')

    # Initialize source node
    dist[source] = 0
    pq = [(0, source)]

    # Loops while pq still has nodes to process
    # Checks previously found distances with new distances and updates accordingly
    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > dist[current_node]:
            continue

        for neighbor, cost in graph[current_node]:
            new_dist = current_dist + cost

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.
    """
    dist_table = {}
    sources = select_sources(spawn, relics, exit_node)

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    answer = (
        "Part 3a:\n"
        " - Stored distanced have been finalized and will never improve. Dijkstra's has already found the shortest path from source to those nodes.\n"
        " - Stored distance is the shortest path found SO FAR using only finalized nodes as steps. This distance could improve as more nodes are finalized.\n"
        "Part 3b:\n"
        " - Source starts with distance 0 b/c no distance from source to source. All other nodes are set to infinity because no paths have been discovered so far.\n"
        " - All edge weights = nonnegative, so unfinalized node with the smallest distance is already at it's shortest route. Distance can't be improved later by some other unfinalized node.\n"
        " - The shortest distance to every reachable node from the source has been calculated. Unreachable nodes remain at infinity (because they can never be reached).\n"
        "Part 3c:\n"
        "Correct distances are important because the Torchbearer will need that information to calculate fuel costs between nodes of interest when comparing different relic orders.\n"
    )
    return answer


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    answer = (
        "Why Greedy Fails:\n"
        " - Greedy choices pick relics without considering how the choice affects the remaining choices and cost. For example, greedy may choose the closest relic first\n"
        " - S -> B costs 1, S -> C costs 3, B <-> C costs 1, B -> T costs 1, C -> T costs 10 \n"
        " - S -> B (1) -> C (1) -> T (10) -> total: 12\n"
        " - S -> C(3) -> B (1) -> T (1) -> total: 5\n"
        " - A locally optimal decision can close off routes for a global optimal solution by putting the Torchbearer in a bad position.\n"
        "What the Algorithm Must Explore:\n"
        " - The algorithm must explore the different possible orders to get relics because the final order is what deteremines total fuel cost.\n"
    )
    return answer


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    best = [float('inf'), []]
    relics_remaining = set(relics)
    relics_visited_order = []

    # Make initial call to explore function
    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        0,
        exit_node,
        best
    )

    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    if cost_so_far >= best[0]:
        # This pruning is safe because all travel costs are nonnegative.
        # A branch whose current cost >= the best complete route cannot become better than the best route found so far..
        return

    # Recusion base case - all relics collected -> go to exit
    if not relics_remaining:
        exit_cost = dist_table[current_loc][exit_node]

        if exit_cost == float('inf'):
            return

        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return

    # Backtracking implementation - remove selected relic
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        # Recursive call
        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

    # Backtracking implementation - add previously selected relic again
        relics_visited_order.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
