class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node
        node.prev = curr

    def append_first(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert(self, data, pos):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        # at pos == 0
        if pos == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return

        # in between or at the end
        curr = self.head
        count = 0
        while curr.next and count < pos - 1:
            curr = curr.next
            count += 1

        node.prev = curr
        node.next = curr.next
        if curr.next:
            curr.next.prev = node
        curr.next = node
        return

    def pop(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next

        curr.next = None

    def pop_left(self):
        self.head = self.head.next
        return

    def reverse(self):
        curr = self.head
        prev_node = None

        while curr:
            # Swap next and prev
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            # Move to next (which is actually prev after swap)
            curr = curr.prev

        # After loop, prev_node will be at the old head's prev
        if prev_node:
            self.head = prev_node.prev


    def display_list(self):
        data = self.head
        while data:
            print(f"{data.data} --> ", end="")
            data = data.next
        else:
            print("None")

    def find_pairs_with_sum(self,  target):
        l, r = self.head, self.head
        while r.next:
            r = r.next

        pairs = []
        while l != r and r.next != l:
            curr = r.data + l.data
            if curr == target:
                pairs.append([l.data, r.data])
                l = l.next
                r = r.prev
            elif curr < target:
                l = l.next
            else:
                r = r.prev
        return pairs

    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return None
        curr = self.head
        while curr and curr.next:
            if curr.val == curr.next.val:
                nextNode = curr.next.next
                curr.next = nextNode
                if nextNode:
                    nextNode.prev = curr
            else:
                curr = curr.next
        return self.head

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(8)
dll.append(9)
# dll.pop()
# dll.pop_left()
# dll.reverse()
dll.display_list()
pairs = dll.find_pairs_with_sum(7)
print(pairs)