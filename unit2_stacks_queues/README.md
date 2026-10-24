## Objective
Implement and analyze two fundamental linear data structures—Stack (LIFO) and Queue (FIFO)—demonstrating their operational mechanics, boundary/edge conditions, and practical application in IT operations workflows.

---

## Implementation

### Stack Class (`Stack`)
Encapsulates Last-In, First-Out (LIFO) ops
* **Operations:**
    * `push()`: Appends an element to the top of the stack.
    * `pop()`: Removes and returns the top element; checks for empty state.
    * `peek()`: Inspects the top element without mutating stack.
    * `is_empty()`: Boolean value returns true if stack empty.
* **Workflow:** Models rollback/undo operational logic by unwinding configuration stages in reverse sequence.

### Queue Class (`Queue`)
Encapsulates First-In, First-Out (FIFO) ops:
* **Operations:**
    * `enqueue()`: Appends an element to the tail of the line.
    * `dequeue()`: Removes leading value and returns it via `popleft()`; checks for empty state.
    * `front()`: Inspects the leading queued element without mutation.
    * `is_empty()`: Boolean value returns true if queue empty.
* **Workflow:** Models an IT service desk ticketing queue, assigning incoming tickets in arrival order.

---

## Reflection

### 1. What concepts or skills did you learn while completing this assignment?
Implementing these structures from the ground up reinforced how abstract data types can be used practically. Utilizing `collections.deque` over a standard list for the queue emphasized time complexity trade-offs, specifically avoiding O(n) element shifting during front-of-list removals. Handling for empty states highlighted the importance of graceful underflow handling rather than letting unhandled index exceptions stop the program early.

### 2. What challenges did you encounter, and how did you overcome them?
The primary challenge was ensuring consistent state checks and clear telemetry during edge-case validation. When inspecting empty collections, unhandled exceptions interrupts downstream processing; implementing safe returns allowed continuous validation of underflow states. Modeling realistic IT administrative scenarios also helped keep console verification intuitive and aligned with operational environments.

### 3. Explain the differences between stacks and queues as this relates to real-world applications.
The core difference lies in LIFO versus FIFO.

* **Stacks (LIFO):** Prioritize the most recent state. This is essential in undo/rollback workflows, call stack execution, transaction backtracking, and packet parsing where the newest operational layer must be resolved or reverted first before reaching earlier baselines.
* **Queues (FIFO):** Enforce chronological processing. This is foundational to asynchronous task assigning, print spooling, network buffer management, and Tier 1 service desk ticket queues, ensuring requests are serviced aligned with submission.