## Objective
Implement and analyze a Binary Search Tree (BST) utilizing recursive operations to manage an enterprise firewall port audit checklist. The implementation explores the mechanics of non-linear trees, comparing recursive searches against linear array structures while validating in-order traversals and edge conditions.

---

## Implementation

### Node Class (`Node`)
* **Value Storage:** Holds port identifier.
* **Pointers:** Initializes left and right child references to `None`.

### Binary Search Tree Class (`BST`)
* **Tree Root:** Top-level hierarchy, starts at `self.root = None`.
* **Recursive Insertion (`insert` / `_insert_recursive`)**:
    * Evaluates target port value against the active node key.
    * Directs smaller values to the left subtree and larger values to the right subtree.
    * Creates a new `Node` upon encountering an empty branch (`None`).
    * Gracefully ignores duplicate values to preserve unique entry constraints in the audit policy.
* **Recursive Search (`search` / `_search_recursive`)**:
    * Halves the active search space at each comparison by branching left or right.
    * Returns `True` on a match or `False` when reaching an empty leaf pointer (`None`).
* **In-Order Traversal (`inorder` / `_inorder_recursive`)**:
    * Recursively visits the left subtree, appends the current node value, and visits the right subtree.
    * Automatically reconstructs port numbers in ascending sorted order.

### Scenario: Firewall Port Audit Registry
* **Policy Ingestion:** Ingests common baseline service ports with Port `80` establishing the root.
* **Search Tests:** Validates active ports return `True`, while confirming inactive ports return `False`.
* **Edge-Case Validation:**
    * **Empty Tree Checks:** Confirms in-order traversal yields an empty list and searching does not throw runtime exception.
    * **Duplicate Ingestion:** Re-inserts Port `80` to verify policy deduplication remains intact during in-order sort.
    * **Single-Node:** Verifies that a single-element tree correctly resolves searches for both existing and missing keys.

---

## Reflection

### 1. What concepts or skills did you learn while completing this assignment?
Implementing recursive operations for insertion, searching, and traversal provided a clear practical demonstration of BST functions. Tracing recursive calls down subtrees clarifies how call stack frames manage state across hierarchical structures. Additionally, observing how in-order traversal flattens a BST into sorted output highlighted the elegance of tree sorting without requiring secondary sorting passes.

### 2. What challenges did you encounter, and how did you overcome them?
The primary challenge was managing recursion base cases and ensuring node references correctly unwind. Returning the updated `node` from `_insert_recursive` and reassigning `node.left` or `node.right` was essential to prevent dropping subtree branches. A late stage addition was made to amend duplicate values in snorting; adding an explicit `else: pass` guard ensured duplicates were safely ignored.

### 3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
A Binary Search Tree enforces strict ordering: every node in a left subtree is less than its parent, and every node in a right subtree is greater. This structural rule creates high efficiency:

* **Unsorted Arrays / Linked Lists:** Searching an unsorted linear structure requires checking every element sequentially O(n) time complexity). A balanced BST eliminates half of the remaining candidate nodes with each comparison, achieving $O(\log n)$ search, insert, and delete performance.
* **Sorted Arrays:** While sorted arrays allow O(log n)searching via binary search, inserting or deleting intermediate elements requires shifting contiguous memory blocks in O(n) time. A BST allows dynamic insertions and deletions in O(log n) time without shifting memory.
* **Traversal Efficiency:** Extracting sorted data from an unsorted list demands an O(n log n) sorting algorithm. In a BST, this reduces to an O(n) complexity as the comparison is already built in.