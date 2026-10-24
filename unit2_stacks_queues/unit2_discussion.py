"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Create an empty array list of items for the stack
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Append new item value to end of list, appended value will be first retrieved
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Notify stack is empty without exiting program
        if self.is_empty():
            return "Cannot remove from empty stack"
        #Removes top value from stack
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Notify stack is empty without exiting program
        if self.is_empty():
            return "Cannot peek empty stack"
        #Return value for top of stack
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self.items


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Appending ensures added values go to tail of the queue to setup FIFO ops
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Notify queue is empty without exiting program
        if self.is_empty():
            return "Cannot remove from empty queue"
        #popleft ensures removal from front of the queue, following FIFO ops
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Notify queue is empty without exiting program
        if self.is_empty():
            return "Queue is empty"
        # Return front value of the queue without changing it
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self.items


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    # Create stack
    stack_demo = Stack()

    # Add 4 values to stack, show peek stack after each push
    stack_demo.push("Install 1")
    print(f"Pushed: {stack_demo.peek()}")
    stack_demo.push("Configure settings 2")
    print(f"Pushed: {stack_demo.peek()}")
    stack_demo.push("Apply license 3")
    print(f"Pushed: {stack_demo.peek()}")
    stack_demo.push("Validate user 4")
    print(f"Pushed: {stack_demo.peek()}")

    #Show LIFO ops by undoing actions until stack is empty
    print("\nRollback for allocation move")
    while not stack_demo.is_empty():
        undo = stack_demo.pop()
        print(f"Rolled back: {undo}")

    print("")
    #Show pop and peek on empty stack
    print(f"Pop on empty stack: {stack_demo.pop()}")
    print(f"Peek on empty stack: {stack_demo.peek()}")

    print("\n== One-value stack ==")
    stack_demo2 = Stack()
    stack_demo2.push("Proof in the pudding")
    print(f"Pushed: {stack_demo2.peek()}")
    stack_demo2.pop()
    print("Stack is now empty: ", stack_demo2.is_empty())



    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    #Create Queue object
    queue_demo = Queue()

    #Add 4 values using enque method, showing front of queue on subsequent adds
    queue_demo.enqueue("Ticket 1: Password reset")
    print(f"Enqueued: Ticket 1")

    queue_demo.enqueue("Ticket 2: Logged into temp profile")
    print(f"Enqueued: Ticket 2 | Current Front of Line: {queue_demo.front()}")

    queue_demo.enqueue("Ticket 3: Disk full")
    print(f"Enqueued: Ticket 3 | Current Front of Line: {queue_demo.front()}")

    queue_demo.enqueue("Ticket 4: Email is down")
    print(f"Enqueued: Ticket 4 | Current Front of Line: {queue_demo.front()}")

    print("")
    # Show FIFO ops by assigning tickets in order they were submitted, emptying queue
    while not queue_demo.is_empty():
        assigned_ticket = queue_demo.dequeue()
        print(f"Assigned to technician: {assigned_ticket}")

    print("")
    #Show Deque and front view on empty queue
    print(f"Dequeue from empty queue: {queue_demo.dequeue()}")
    print(f"Front of empty queue: {queue_demo.front()}")

    print("\n== One-value queue ==")
    queue_demo2 = Queue()
    queue_demo2.enqueue("Ticket 1: Password reset")
    print(f"Enqueued single ticket: {queue_demo2.front()}")
    queue_demo2.dequeue()
    print("Queue is empty: ", queue_demo2.is_empty())


if __name__ == "__main__":
    main()
