"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)
    #Starting from replaced index, all values are shifted one-right
    #The closer to index 0, O(n) complexity and worst case, the greater the performance hit
    #Insertion at final index is (1), best case scenario


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if -len(lst) <= index < len(lst):
        return lst.pop(index)
    #supports standard and negative indices
    #Validating indices prevents termination when error is raised
    #Elements are shifted one-left from where removal occurs
    return None
    #Nothing happens if index not valid


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    #Searches from 0 to end and first hit of value is returned
    #Subsequent matches will not be returned from this
    #O(n) complexity, worst case is a value not found, best is index 0
    return -1
    #returns sentinel value if the index value is not found


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n\n=== INSERTION TESTS ===")

    servers = ["prd-dc02", "prd-fs02", "prd-wsus01"]
    print(f"Original Server List: {servers}")

    # Adding Domain Controller at 0 shifts all values to the right.
    insert_at(servers, 0, "prd-dc01")
    print(f"After inserting [prd-dc01] at BEGINNING: {servers}")

    # Adding File Server between prd-dc02 and prd-fs02 shifts downstream values right.
    insert_at(servers, 2, "prd-fs01")
    print(f"After inserting [prd-fs01] in the MIDDLE: {servers}")

    # Appending Print server does not require shifting.
    insert_at(servers, len(servers), "prd-prt01")
    print(f"After inserting [prd-prt01] at the END: {servers}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    # Removing head shifts all remaining values one-left.
    remove_start = delete_at(servers, 0)
    print(f"\nRemoved from BEGINNING: {remove_start}")
    print(f"Updated List: {servers}")

    # Removing prd-fs01 shifts values at indices 2 and above one-left.
    remove_middle = delete_at(servers, 1)
    print(f"\nRemoved from MIDDLE: {remove_middle}")
    print(f"Updated List: {servers}")

    # Removing the tail does not require shifting.
    removed_end = delete_at(servers, -1)
    print(f"\nRemoved from END: {removed_end}")
    print(f"Updated List: {servers}")

    # List is effectively back to point of creation

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n\n=== SEARCH TESTS ===")
    search01 = "prd-wsus01"
    hit = search_value(servers, search01)
    print(f"\nSearching for existing host '{search01}'\n"
          f"        Found at index {hit}")

    search02 = "prd-prt01"
    miss = search_value(servers, search02)
    print(f"\nSearching for decommissioned host '{miss}'\n"
          f"        Not found - Return code: {miss})")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n\n=== EDGE CASES ===")

    #Empty list for demo
    serverless_doom = []

    # Out-of-bounds deletion using server list
    # Should return None instead of IndexError
    oob_delete = delete_at(servers, 5)
    print(f"\nDelete invalid index [5]: Result = {oob_delete}")

    # Deletion from an empty list
    # Validation will occur, should prevent pop() crashing program.
    empty_delete = delete_at(serverless_doom, -1)
    print(f"\nDelete index from empty list: Result = {empty_delete}")

    # Search an empty list
    # Validation will occur, loop should terminate and return -1.
    empty_search = search_value(serverless_doom, "prd-dc01")
    print(f"\nSearch empty list: Result = {empty_search}")

    #Insert into empty list or out of bounds
    #Out-of-bounds insertions act as an appendation
    insert_at(serverless_doom, 99, "prd-wsus01")
    print(f"\nAfter insert at out-of-bounds index 99: {serverless_doom}")


if __name__ == "__main__":
    main()