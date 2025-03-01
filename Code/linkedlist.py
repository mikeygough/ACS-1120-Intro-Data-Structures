#!python


class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f"Node({self.data})"


class LinkedList:
    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f"({item}) -> "
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        node = Node(item)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list."""
        node = Node(item)

        if self.is_empty():
            self.tail = node
        node.next = self.head
        self.head = node

    def find(self, matcher):
        """Return an item from this linked list if it is present."""
        node = self.head

        while node is not None:
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        node = self.head
        previous = None

        while node is not None:
            if node.data == item:
                # head
                if previous is None:
                    self.head = node.next
                    # 1 element
                    if node.next is None:
                        self.tail = None
                else:
                    previous.next = node.next
                    # tail
                    if node.next is None:
                        self.tail = previous
                return

            previous = node
            node = node.next

        raise ValueError(f"Item not found: {item}")

    def replace(self, old_item, new_item):
        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next


def test_linked_list():
    ll = LinkedList()
    print("list: {}".format(ll))
    print("\nTesting append:")
    for item in ["A", "B", "C"]:
        print("append({!r})".format(item))
        ll.append(item)
        print("list: {}".format(ll))

    print("head: {}".format(ll.head))
    print("tail: {}".format(ll.tail))
    print("length: {}".format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print("\nTesting delete:")
        for item in ["B", "C", "A"]:
            print("delete({!r})".format(item))
            ll.delete(item)
            print("list: {}".format(ll))

        print("head: {}".format(ll.head))
        print("tail: {}".format(ll.tail))
        print("length: {}".format(ll.length()))


if __name__ == "__main__":
    test_linked_list()
