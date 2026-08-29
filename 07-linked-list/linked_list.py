class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self) -> None:
        self.length = 0
        self.head = None
        # tail pointer keeps add() at O(1); walking to the end each time is O(n squared)
        self.tail = None

    def is_empty(self) -> bool:
        return self.length == 0

    def add(self, element) -> None:
        node = self.Node(element)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def remove(self, element) -> None:
        """Unlink the first node holding this element. Does nothing if absent."""
        previous_node = None
        current_node = self.head

        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

        if current_node is self.tail:
            self.tail = previous_node

        self.length -= 1

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.element
            current_node = current_node.next

    def __repr__(self) -> str:
        return f"LinkedList({list(self)})"


if __name__ == "__main__":
    my_list = LinkedList()
    print(my_list.is_empty())

    my_list.add(1)
    my_list.add(2)
    print(my_list.is_empty())
    print(len(my_list))

    my_list.remove(1)
    print(my_list)
