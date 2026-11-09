"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    iterations = 0
    for index in range(len(lst)):
        iterations += 1
        if lst[index] == target:
            return index, iterations
    return -1, iterations

    # Linear search runs O(n) sequential scan of elements
    # from index 0 to tail. Order of elements does not matter.
    # If index is not found the search has encountered worst
    # case performance scenario; all elements were inspected.

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    iterations = 0
    low = 0
    high = len(lst) - 1
    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid, iterations
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, iterations

    # Binary search keeps pointers to space to be
    # searched using low and high. This search requires
    # data be sorted to execute properly. The mid-point
    # evaluates if target matches. A match is returned
    # immediately. O(log n) complexity is achieved by
    # eliminating half of the pool on each iteration
    # if target is lower or higher than mid.


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # sorted array of ticket numbers
    sorted_inc_tickets = [1042, 1055, 1080, 1092, 1105, 1120, 1145, 1199, 1206]
    print(f"Opened and unassigned incidents: {sorted_inc_tickets}")
    # targets for a hit and a miss on searches
    target_hit = 1105
    target_miss = 1200

    # Tests for target match, display index
    lin_hit_idx, lin_hit_iters = linear_search(sorted_inc_tickets, target_hit)
    bin_hit_idx, bin_hit_iters = binary_search(sorted_inc_tickets, target_hit)
    print(f"\nSearch for incident {target_hit}...")
    print(f"  Linear index {lin_hit_idx} found in {lin_hit_iters} iterations")
    print(f"  Binary index {bin_hit_idx} found in {bin_hit_iters} iterations")

    # Tests for miss, display index, -1 return means does not exist
    # Linear search scanned all elements, binary scanned midpoints
    lin_miss_idx, lin_miss_iters = linear_search(sorted_inc_tickets, target_miss)
    bin_miss_idx, bin_miss_iters = binary_search(sorted_inc_tickets, target_miss)
    print(f"\nSearch for incident {target_miss}...")
    print(f"  Linear index {lin_miss_idx} finished in {lin_miss_iters} iterations")
    print(f"  Binary index {bin_miss_idx} finished in {bin_miss_iters} iterations")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # Much larger array of 50,000 tickets
    historical_incidents = list(range(1, 50001))
    print(f"Historical incident count: {len(historical_incidents)}")

    # Search for incident on back half to show performance improvement
    search_for_inc = 41213

    lin_idx, lin_iters = linear_search(historical_incidents, search_for_inc)
    bin_idx, bin_iters = binary_search(historical_incidents, search_for_inc)

    # Show index and iterations required to reach it
    print(f"\nSearch for historical incident {search_for_inc}...")
    print(f"  Linear index {lin_idx} found in {lin_iters:,} iterations")
    print(f"  Binary index {bin_idx} found in {bin_iters} iterations")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("Values in parenthesis are index and iterations respectively")

    # Empty queue
    empty_queue = []
    print(f"Empty queue search \n    "
          f"Linear={linear_search(empty_queue, 1)}\n    "
          f"Binary={binary_search(empty_queue, 1)}")

    # Hit and miss on a single ticket
    single_ticket = [1]
    print(f"Single element hit \n    "
          f"Linear: {linear_search(single_ticket, 1)} \n    "
          f"Binary: {binary_search(single_ticket, 1)}")
    print(f"Single element miss \n    "
          f"Linear: {linear_search(single_ticket, 9999)} \n    "
          f"Binary: {binary_search(single_ticket, 9999)}")

    # Ticket at front boundary
    print(f"Search on head boundary \n    "
          f"Linear: {linear_search(sorted_inc_tickets, sorted_inc_tickets[0])} \n    "
          f"Binary: {binary_search(sorted_inc_tickets, sorted_inc_tickets[0])}")


if __name__ == "__main__":
    main()