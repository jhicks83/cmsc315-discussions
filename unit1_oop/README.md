## Objective
Create a basic IT asset tracking system to be used in tandem with help desk operations, configuration management, and hardware lifecycle tracking.

---

## Implementation

### Parent Class (`Asset`)
Represents the enterprise baseline desktop computer:
* **Class Variable:** Baseline operating system (`Win 11 Enterprise`) shared across fleet assets.
* **Instance Variables:** Individual asset tag, assigned user/location, and a baseline software configuration dictionary.
* **Display Method:** Returns a structured summary of the workstation's configuration and assignment.

### Child Class (`DesignerWorkstation`)
Represents specialized hardware provisioned for high-compute workloads:
* **Inheritance:** Inherits all core configuration attributes from `Asset`.
* **Class Variable:** Hardware baseline specification for dedicated GPU.
* **Instance Variables:** Expanded storage and memory capacity.
* **Child Method:** Adds application packages directly into the active software configuration.
* **Method Overriding:** Overrides the parent display method to append specs without rewriting base logic.

---

## Reflection

### 1. What concepts or skills did you learn while completing this assignment?
Following the structured TODOs helped reinforce practical object-oriented design and inheritance patterns in Python. Implementing the shallow and deep copy demonstrations bridged the gap between high-level OOP and computer architecture/memory concepts. Specifically, seeing how compound objects point to the same nested memory addresses clarified object references under the hood.

### 2. What challenges did you encounter, and how did you overcome them?
One initial challenge was getting used to version control workflows in IntelliJ when pushing the starter code to GitHub. Another challenge was presenting clear, readable console output without relying on a GUI. The most critical conceptual hurdle was separating attribute rebinding from in-place mutation when analyzing shallow and deep copies. Reviewing how an instance's local `__dict__` isolates top-level attribute assignments—while nested mutable containers still share underlying memory addresses—helped solidify the distinction.

### 3. Compare OOP to procedural programming.
Procedural programming structures code around step-by-step procedures or sequential routines that act upon passive data. While straightforward for linear tasks, it often leads to tight coupling, making the codebase harder to maintain, test, and scale.
OOP shifts the focus to self-contained entities objects that bundle data and methods. By encapsulating functionality and establishing clear relationships through inheritance and polymorphism, OOP abstracts away implementation details, reduces duplicate logic, and makes large software systems far more modular and extensible.

### 4. Discuss the benefits of maintainability and reusability and apply this to managing overhead, practical application development, and future use.
Maintainability and reusability directly reduce development friction, operational overhead, and long-term technical debt:

* **Managing Overhead:** In a procedural or copy-paste architecture, changing a standard policy (such as updating an OS version or base software package) requires locating and modifying every instance manually—a process prone to regressions and costly debugging. In an OOP model, modifying the parent class immediately propagates improvements to all child classes and reduces maintenance.
* **Practical Application Development:** Code reuse eliminates redundancy. Tried and tested blocks can be extended rather than starting from scratch.
* **Future Use and Extensibility:** If the enterprise introduces virtual desktops, engineers can potentially inherit from `Asset` or implement shared interfaces without refactoring the existing codebase.