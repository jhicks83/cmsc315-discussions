# Unit 6 Discussion: Python Dictionaries as Hash Tables

## Overview
This assignment explores how Python dictionaries operate internally as open-addressed hash tables. Using a active virtual machine session management scenario, the implementation demonstrates operations, handles missing-key edge cases safely, and analyzes how hash collisions and probing mechanics affect runtime efficiency.

---

## Implementation
* **Insert** Initialized an empty dictionary and populated five active host records. Python passes each immutable hostname string through its built-in `hash()` function to compute a target bucket index, inserting the tuple reference.
* **Lookup** Retrieved active session tuples through direct key indexing. Hashing the hostname jumps directly to its space in memory.
* **Update** Reassigned `"vm-web-prod01"` from `"j.doe"` to `"m.hicks"`. Because hash table keys are unique, the tuple reference of the existing key is replaced without creating duplicate entries.
* **Delete** Simulated a user logoff `.pop()`. Removing an entry clears the key-value reference while leaving a tombstone marker so that probe chains for colliding hostnames do not terminate prematurely.
* **Edge Cases**
  * **Missing Key Lookup:** Querying an idle host via `.get()` safely returns None instead of crashing with a KeyError.
  * **Missing Key Deletion:** Calling `.pop()` with a fallback tuple makes session cleanup consistent when a host is already idle.
  * **Upsert:** Assigning a tuple to an unprovisioned hostname seamlessly hashes the new key and allocates a fresh table entry.

---

## Performance Analysis

### How Collisions Impact Efficiency
Under ideal conditions with uniform key distribution, hash table ops execute in O(1) constant time; however, because a finite array of memory buckets maps to an infinite space of possible string keys, two hostnames can produce the same initial slot index.
* **Impact on Lookup Speed:** Each collision along a probe sequence forces additional key comparisons. As the table's load factor increases, probe chains grow longer, shifting average lookup time away from pure O(1) toward linear O(n) in the worst-case scenario.
* **Dynamic Resizing Mitigation:** To prevent severe performance degradation, Python resizes and rehashes the table into a larger memory allocation once the load factor reaches roughly two-thirds capacity.

---

## Discussion Board Reflection

### 1. Design Approach & Hash Table Application
Modeling active VM user sessions provided a clear demonstration of why hash tables are foundational in systems engineering and auditing. Pairing immutable VM hostnames as keys with essential values such as hostnames and account types kept the data model structured while showcasing how Python hashes string keys to memory for O(1) retrieval. Using methods like `.get()` and `.pop()` with fallbacks ensured that querying idle hosts or revoking expired sessions handled missing keys cleanly.

### 2. Hash Functions & Collision Resolution Trade-offs
Working through Python's deletion mechanics clarifies how open addressing functions. Rather than storing collisions in linked lists, open addressing keeps all entries inside the table array and relies on probe sequences to resolve collisions. Because resetting a deleted slot to empty would break the search path for subsequent colliding keys, removed entries are marked as tombstones until the next resize. This does lead to periodic O(n) table resizing to keep the load factor low and probe chains short.