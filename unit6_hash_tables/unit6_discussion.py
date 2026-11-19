"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    # Python dictionaries function as hash tables.
    # When inserting an entry, Python runs the immutable string key through
    # its built-in hash() function to calculate a specific memory bucket index
    # allowing O(1) average-case ops.

    # Create empty dictionary
    vm_sessions = {}

    # Insert 5 active VM sessions mapping
    # Hostname (key) | Username, Account Type tuple (tuple values)
    vm_sessions["vm-user-prod01"] = ("j.doe", "Standard User")
    vm_sessions["vm-dc-core01"] = ("a.smith", "Domain Admin")
    vm_sessions["vm-adm-eph01"] = ("m.jones", "Local Admin")
    vm_sessions["vm-user-prod02"] = ("r.evans", "Standard User")
    vm_sessions["vm-user-prod03"] = ("l.chen", "Standard User")

    print("Active VM Session Table:")
    for hostname, (username, account_type) in vm_sessions.items():
        print(f"  {hostname:<15} User: {username:<10} Account Type: {account_type}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    # Looking up hostname such as "vm-web-prod01" hashes hostname
    # and jumps directly to its memory space. This ensures O(1)
    # constant-time lookups.
    dc_user, dc_role = vm_sessions["vm-dc-core01"]
    db_user, db_role = vm_sessions["vm-adm-eph01"]

    print(f"Lookup: 'vm-dc-core01' \n"
          f"User: {dc_user} ({dc_role})")
    print(f"\nLookup: 'vm-adm-eph01' \n"
          f"User: {db_user} ({db_role})")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    target_vm = "vm-adm-eph01"

    # Because hash table keys must remain unique, assigning a new tuple
    # to an existing VM hostname hashes to the same bucket and overwrites the
    # value. No duplicate is created, preserving O(1) speed.

    old_user, old_role = vm_sessions[target_vm]
    print(f"{'Before update:':<14} {target_vm:<12}  User={old_user} ({old_role})")

    #Simulate original user has signed off, provision same hostname to new user
    vm_sessions[target_vm] = ("m.hicks", "Standard User")

    new_user, new_role = vm_sessions[target_vm]
    print(f"{'After update:':<14} {target_vm:<12}  User={new_user} ({new_role})")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    # When a user logs off a VM, .pop() hashes the hostname to find its slot,
    # removes the tuple, and leaves an empty-after-removal marker in the table.
    # This preserves open-addressing probe chains so subsequent lookups for
    # colliding hostnames do not terminate.

    logoff_vm = "vm-adm-eph01"
    print(f"Active VM session count before logoff on '{logoff_vm}': {len(vm_sessions)}")
    print(f"Active hostnames before: {list(vm_sessions.keys())}")

    #Call .pop() to update the table
    ended_user, ended_role = vm_sessions.pop(logoff_vm)

    print(f"\nLogged off '{logoff_vm}' -> Removed session for {ended_user} ({ended_role})")
    print(f"\nActive VM session count after logoff: {len(vm_sessions)}")
    print(f"Active hostnames after:  {list(vm_sessions.keys())}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Using .get() on a non-existent hostname returns None
    idle_vm = "vm-fake-00"
    session_check = vm_sessions.get(idle_vm)
    print(f"Lookup for idle host '{idle_vm}': {session_check}")

    # Using .pop() on session that is not currently active.
    # Passing a fallback tuple to .pop() prevents KeyError
    clear_result = vm_sessions.pop(idle_vm, ("N/A", "Host has no active session"))
    print(f"\nLogoff clear for '{idle_vm}': {clear_result[1]}")

    # Assigning a tuple to a hostname not yet present hashes the new key
    # and inserts a fresh entry into the table without error.
    new_vm = "vm-sec-siem01"
    vm_sessions[new_vm] = ("s.chief", "CISO")
    print(f"\nNew VM provisioned: {new_vm:<15} User={vm_sessions[new_vm][0]} ({vm_sessions[new_vm][1]})")


if __name__ == "__main__":
    main()