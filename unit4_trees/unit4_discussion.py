"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)
        # BST logic demands that each node in the left subtree
        # of a parent node be smaller than the parent, and each
        # node of the right subtree be larger than the parent.
        # Comparing the new value starting from parent node
        # helps determine new node's placement in tree.

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Establish base case
        if node is None:
            return Node(value)
        # if value for less than recursion
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # elif value for greater than recursion
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # ignores duplicate value
        else:
            pass
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)
        # As a list of values grows, the O(n) complexity of a
        # linear search can bog down the program, the primary
        # benefit of the BST is that each comparison cuts
        # the remainder by half, down to O(log n) complexity

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base cases for no node or immediate hit
        if node is None:
            return False
        if node.value == value:
            return True

        # Search branches left if target is smaller
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Search branches right if target is larger
        if value > node.value:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        bst_values = []
        self._inorder_recursive(self.root, bst_values)
        return bst_values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Base case of non-empty node
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)
        # BST values are sorted in ascending order because
        # left subtree values are smaller than node's value,
        # and right subtree values are larger than node's
        # value, ensuring smallest to greatest ordering


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    # Initializes the BST
    port_tree = BST()
    # Port numbers to be inserted
    monitored_ports = [80, 22, 443, 53, 25, 445, 67, 3389, 8080]
    # Loop through numbers, adding to BSt
    print(f"Ports in firewall audit tree: {monitored_ports}")
    for port in monitored_ports:
        port_tree.insert(port)
    # Starting from root 80, search branches left or
    # right based on target value, eliminating O(n)
    # linear search, beneficial to larger lists

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_ports_inorder = port_tree.inorder()
    print(f"Ports in inorder traversal: {sorted_ports_inorder}")
    # Leaves are visited sequentially in root node's left subtree,
    # then root node is visited, and then leaves are visited
    # sequentially in root node's right subtree

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("Returns True on hit, False on miss")

    print(f"Is Port 443 found? | {port_tree.search(443)}")
    print(f"Is Port 8080 found? | {port_tree.search(8080)}")

    print(f"Is Port 123 found? | {port_tree.search(123)}")
    print(f"Is Port 3306 found? | {port_tree.search(3306)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    # Create empty BST
    empty_tree = BST()

    # Runs inorder method on empty tree, does not crash
    # due to base case being met by default
    print(f"Empty host tree traversal: {empty_tree.inorder()} "
          f"\n  There are no nodes.")

    # Search for a port on empty tree should return False without crashing
    print(f"\nSearching Port 443 on empty tree: {empty_tree.search(443)} ")

    # Inserts duplicate value, should not duplicate in traversal
    port_tree.insert(80)
    print(f"\nInserting duplicate Port 80..."
          f"\nSorted list after duplicate: {port_tree.inorder()}")

    # Create tree with one node only; sort it, search for 22 and false node
    single_node_tree = BST()
    single_node_tree.insert(22)
    print(f"\nTree with single node of Port 22: {single_node_tree.inorder()}")
    print(f"   Search existing (22): {single_node_tree.search(22)}")
    print(f"   Search non-existing (80): {single_node_tree.search(80)}")


if __name__ == "__main__":
    main()