## Objective
Evaluate and benchmark linear search and binary search algorithms. Using an IT service desk incident ticket scenario, the implementation traces step-by-step iteration counts across both small and large datasets, explores algorithm performance boundaries, and analyzes trade-offs involving data sortedness and computational overhead.

---

## Implementation

### Linear Search (`linear_search`)
* **Iteration Tracking:** Initializes and increments counter to record comparison steps.
* **Traversal:** Inspects items sequentially from index `0` to `len(lst) - 1`.
* **Hit Evaluation:** Terminates immediately upon matching the target value and returns index of hit.
* **Miss:** Returns sentinel on a miss.

### Binary Search (`binary_search`)
* **Iteration Tracking:** Initializes and increments counter to record comparison steps.
* **Pointers:** Establishes lower and upper window bounds using `low = 0` and `high = len(lst) - 1`.
* **Midpoint:** Calculates the integer midpoint (`mid = (low + high) // 2`) on each iteration.
* **Search Window:**
    * If `lst[mid] == target`, returns hit index.
    * If `lst[mid] < target`, eliminates the lower half by adjusting `low = mid + 1`.
    * If `lst[mid] > target`, eliminates the upper half by adjusting `high = mid - 1`.
* **Loop Termination & Miss:** If boundaries cross without a match, returns sentinel on a miss.

---

## Discussion Board Reflection

### 1. What concepts or skills did you learn while completing this assignment?
Tracking iteration counts provided a clear demonstration of algorithmic complexity, making the mathematical difference between O(n) linear scaling and O(log n) logarithmic reduction obvious. Seeing a linear search require over 40,000 checks while binary search resolved the identical record in only 15 steps demonstrates how divide-and-conquer logic often eliminates large portions of search space. I also gained a better understanding of boundary behaviors, specifically seeing why linear search occasionally outperforms binary search at the immediate head of an array due to starting position.

### 2. What challenges did you encounter, and how did you overcome them?
My primary challenge was setting up a tracker for iterations alongside return indices without breaking the sentinel contract. Initially, returning a tuple required updating the test print statements to unpack the values properly so the output clearly distinguished the target's index from the iteration count. Additionally, working through the boundary edge cases reinforced the importance of integer division over true division to ensure off-by-one errors do not occur when narrowing down to a single element.

### 3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
Linear search is ideal for small, unsorted, or often-changing collections such as a live IT helpdesk queue where tickets are constantly appended, modified, or closed. Because binary search strictly requires sorted data, sorting an unorganized dataset introduces an O(n log n) cost. If search frequency is low, that sorting overhead outweighs the efficiency of binary search, making an O(n) linear scan faster overall.

Binary search is the superior choice for large, static or pre-sorted datasets such as an enterprise asset registry or historical incident database. When datasets scale to tens of thousands of records, repeated searches justify the initial sort, as O(log n) retrieval ensures faster lookups that prevent application bottlenecks.