"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Asset:
    default_os = "Win 11 Enterprise"

    def __init__(self, asset_tag: str, assigned_to: str):
        self.asset_tag = asset_tag
        self.assigned_to = assigned_to
        self.config = {
            "installed_software": ["Chrome Browser", "Office 365", "Adobe Reader"]
        }

    def get_asset_details(self):
        return (
            f"[OS: {Asset.default_os}] Tag: {self.asset_tag} | "
            f"Assigned To: {self.assigned_to} | "
            f"Software: {self.config['installed_software']}"
        )

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class DesignerWorkstation(Asset):
    discrete_gpu = False

    def __init__(self, asset_tag: str, assigned_to: str, storage: int = 2000, memory: int = 32):
        super().__init__(asset_tag, assigned_to)
        self.storage = storage
        self.memory = memory

    def add_software(self, software_name: str):
        self.config["installed_software"].append(software_name)
        return f"Allocated '{software_name}' onto {self.asset_tag}."

    def get_asset_details(self):
        base_details = super().get_asset_details()
        return (
            f"{base_details} | RAM: {self.memory} GB | "
            f"Storage: {self.storage} GB | Discrete GPU: {DesignerWorkstation.discrete_gpu}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first_object = DesignerWorkstation("WS-DES-11", "Billy Bob", memory=64)
    second_object = DesignerWorkstation("WS-DES-12", "Jojo Mayer", storage=4000)
    print(f"Class var through class: {DesignerWorkstation.discrete_gpu}")
    print(f"Class var through object instance: {first_object.discrete_gpu}")
    first_object.dual_monitors = True
    print("First object namespace:\n", first_object.__dict__)
    print("Second object namespace:\n", second_object.__dict__)
    print("Class namespace:\n", DesignerWorkstation.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original_workstation = DesignerWorkstation("WS-STA-101", "Unassigned", memory=64)
    shallow_ws = copy(original_workstation)
    deep_ws = deepcopy(original_workstation)
    original_workstation.assigned_to = "Onboarding Lead"
    original_workstation.config["installed_software"].append("Blender")

    print(f"Original : Assigned={original_workstation.assigned_to} | Software={original_workstation.config['installed_software']}")
    # We see that the shallow copy has its own namespace, so rebinding assigned_to does not affect it,
    # but in-place mutation of the shared nested list does reflect.
    print(f"Shallow  : Assigned={shallow_ws.assigned_to} | Software={shallow_ws.config['installed_software']}")
    # We see the deep copy occupies its own space in memory as it maintains an exact replica
    # of original_workstation as it was when the copy was created
    print(f"Deep     : Assigned={deep_ws.assigned_to} | Software={deep_ws.config['installed_software']}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Class demonstration ===")
    standard_asset = Asset(asset_tag="WS-STA-001", assigned_to="Front office hot desk")
    print(standard_asset.get_asset_details())

    print("\n=== Child Class object demonstration ===")
    lead_ws = DesignerWorkstation(asset_tag="WS-DES-99",assigned_to="Sarah Connor", storage=4000, memory=64)
    print(lead_ws.get_asset_details())
    print(lead_ws.add_software("Skynet"))
    print(f"Updated software allocations: {lead_ws.config['installed_software']}")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()