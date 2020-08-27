class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return None
        # Checking if linked list has only one node.
        if self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value  # save current value
        current = self.head
        # Once check is finished and determines there
        # is more than one node, move to else
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        return value
