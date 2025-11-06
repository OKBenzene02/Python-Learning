# """
# Implementation of Linked Lists
# Date - 23 - 04 - 23
# """
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
# # # Add element at the beginning
#     def pushleft(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
# # # Add element after a specified element
#     def add(self, prev, new):
#         new_node = Node(new)
#         if not self.head:
#             return
#
#         if prev == self.head.data:
#             new_node.next = self.head.next
#             self.head.next = new_node
#             return
#
#         head = self.head
#         while head.data != prev:
#             head = head.next
#             if not head:
#                 return
#         new_node.next = head.next
#         head.next = new_node
#
# # # Add element at a specified index
#     def insert(self, index, data):
#         new_node = Node(data)
#         if not self.head:
#             return
#
#         if index == 0 and self.head:
#             new_node.next = self.head.next
#             self.head.next = new_node
#             return
#
#         head = self.head
#         while head and index > 1:
#             head = head.next
#             if not head:
#                 return
#             index -= 1
#         new_node.next = head.next
#         head.next = new_node
#
# # # Add element at the end
#     def append(self, data):
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#             return
#
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#
# # # To check whether the element is in the linked list
#     def isPresent(self, ele):
#         temp = self.head
#         while temp:
#             if temp.data == ele:
#                 return True
#             temp = temp.next
#         return False
#
# # # To get the element based on the index
#     def get(self, index):
#         temp = self.head
#         if index == 0 and temp:
#             return temp.data
#
#         while temp and index > 0:
#             temp = temp.next
#             index -= 1
#         return temp.data
#
# # # Calculate the length of the linked list
#     def length(self):
#         count = 0
#         curr = self.head
#         while curr:
#             count += 1
#             curr = curr.next
#
#         return count
#
# # # Reverse a linked list
#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         self.head = prev
#
# # # Deleting an element based on the position
#     def deleteIDX(self, pos):
#         if not self.head:
#             return
#         temp = self.head
#         prev = self.head
#         for i in range(pos):
#             if i == 0 and pos == 1:
#                 self.head = self.head.next
#             else:
#                 if i == pos - 1 and temp:
#                     prev.next = temp.next
#                 else:
#                     prev = temp
#                     if not prev:
#                         break
#                     temp = temp.next
#
# # # Sorting a linked list using merge sort o(nlogn)
#     def sort(self, l, r):
#         merged = Node(-1)
#         temp = merged
#
#         while l and r:
#             if l.data < r.data:
#                 temp.next = l
#                 l = l.next
#             else:
#                 temp.next = r
#                 r = r.next
#             temp = temp.next
#
#         while l:
#             temp.next = l
#             l = l.next
#             temp = temp.next
#
#         while r:
#             temp.next = r
#             r = r.next
#             temp = temp.next
#         return merged.next
#
#     def mergeSort(self, temp):
#         if temp is None or temp.next is None:
#             return temp
#
#         mid = self.middle(temp)
#         nxt = mid.next
#         mid.next = None
#         return self.sort(self.mergeSort(temp), self.mergeSort(nxt))
#
#     def middle(self, temp):
#         hare, tort = temp.next, temp
#         while hare and hare.next:
#             hare = hare.next.next
#             tort = tort.next
#         return tort
#
# # # Display the linked list
#     def show(self, head):
#         while head:
#             print(head.data, "-- ",end="")
#             head = head.next
#         print()
#
# ll = LinkedList()
# ll.append(4)
# ll.append(1)
# ll.append(3)
# ll.append(23)
# ll.append(6)
# ll.mergeSort(ll.head)
# # print(ll.middle(ll.head))
# ll.show(ll.head)
#
#
#

# class Node:
#
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     # # Adding data at the beginning
#     def pushleft(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#
#     def insertPos(self, prev, data):
#         new_node = Node(data)
#         if not self.head: return
#         head = self.head
#         if prev == head.data:
#             new_node.next = head.next
#             head.next = new_node
#             self.size += 1
#             return
#
#         while head.data != prev:
#             head = head.next
#             if not head: return
#
#         new_node.next = head.next
#         head.next = new_node
#         self.size += 1
#
#     def insertIdx(self, idx, data):
#         new_node = Node(data)
#         if not self.head: return
#         head = self.head
#         if idx == 0 and self.head:
#             new_node.next = head.next
#             head.next = new_node
#             self.size += 1
#             return
#
#         while head and idx > 1:
#             head = head.next
#             if not head: return
#             idx -= 1
#         new_node.next = head.next
#         head.next = new_node
#         self.size += 1
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.size += 1
#             return
#
#         head = self.head
#         while head.next:
#             head = head.next
#         head.next = new_node
#         self.size += 1
#
#     def reverse(self):
#         prev, curr = None, self.head
#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         self.head = prev
#
#     def deleteAt(self, pos):
#         if not self.head: return
#         idx = 0; curr = self.head; prev = None
#         while curr.next and idx < pos:
#             prev = curr
#             curr = curr.next
#             idx += 1
#         if idx < pos: return
#         elif idx == 0: self.head = self.head.next
#         else: prev.next = curr.next
#         self.size -= 1
#
#     def isPresent(self, ele):
#         temp = self.head
#         while temp:
#             if temp.data == ele: return True
#             temp = temp.next
#         return False
#
#     # # Display the linked list
#     def show(self, head):
#         while head:
#             print(head.data, "-- ",end="")
#             head = head.next
#         print()
#
#
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# # ll.insertPos(4, 5)
# # ll.insertPos(5, 6)
# # ll.insertPos(6, 7)
# # ll.insertPos(7, 8)
# # ll.insertIdx(2, 10)
# # ll.pushleft(23)
# # ll.insertPos(3,6)
# # ll.mergeSort(ll.head)
# # print(ll.middle(ll.head))
# ll.show(ll.head)
# print(ll.size)
# # ll.deleteAt(ll.size - 1)
# # ll.show(ll.head)
# # print(ll.size)
# # ll.deleteAt()
# # ll.show(ll.head)
# # print(ll.isPresent(4))


class Node:

    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data: int):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def append_left(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        new.next = self.head
        self.head = new

    def pop(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None

    def pop_left(self):
        if not self.head:
            return
        self.head = self.head.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def insert(self, data, pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return

        count = 0
        curr = self.head
        while curr and count < pos - 1:
            curr = curr.next
            count += 1

        if not curr:
            curr = self.head
            while curr:
                curr = curr.next
            curr.next = new
            return

        new.next = curr.next
        curr.next = new

    def add_two_numbers(self, l1, l2):
        temp = Node(0)
        carry = 0
        curr = temp
        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            total %= 10
            node = Node(total)
            curr.next = node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return temp.next

    def sort_linked_list(self):
        zeroDummy, oneDummy, twoDummy = Node(-1), Node(-1), Node(-1)
        zeroHead, oneHead, twoHead = zeroDummy, oneDummy, twoDummy
        curr = self.head
        while curr.next:
            node = Node(curr.data)
            if curr.data == 0:
                zeroHead.next = node
                zeroHead = zeroHead.next
            elif curr.data == 1:
                oneHead.next = node
                oneHead = oneHead.next
            else:
                twoHead.next = node
                twoHead = twoHead.next
            curr = curr.next
        zeroHead.next = oneDummy.next if oneDummy.next else twoDummy.next
        oneHead.next = twoDummy.next
        return zeroDummy.next

    def odd_even_ll(self):
        if not self.head: return
        odd = self.head; even = self.head.next; evenHead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return self.head

    def remove_nth(self, n):
        if not self.head: return
        fast = self.head
        for _ in range(n):
            fast = fast.next
        slow = self.head
        if not fast:
            return self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next
        return self.head

    def check_palindrome(self):
        if not self.head or not self.head.next: return True

        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        slow1 = self.head
        slow = prev
        while slow:
            if slow.data != slow1.data: return False
            slow = slow.next
            slow1 = slow1.next
        return True

    def middle_element(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def rotat_linked_list(self, k):
        n = 1
        temp = self.head
        while temp.next:
            temp = temp.next
            n += 1

        k = k % n
        if not k: return self.head

        curr = self.head
        for _ in range(n - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None
        temp.next = self.head
        return newHead

    @staticmethod
    def print_linked_list(data):
        while data:
            print(f"{data.data} --> ", end="")
            data = data.next
        else:
            print("None")

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.append(5)
# ll.append_left(6)
# ll.append_left(7)
# LinkedList.print_linked_list(ll.head)
# ll.reverse()
# print()
# LinkedList.print_linked_list(ll.head)
# print()
# ll.insert(10, 0)  # Insert at head
# ll.insert(20, 1)  # Insert at end
# ll.insert(15, 1)  # Insert at position 1 (middle)
# LinkedList.print_linked_list(ll.head)

# ll1 = LinkedList()
# ll2 = LinkedList()
# ll1.append(2)
# ll1.append(4)
# ll1.append(3)
# LinkedList.print_linked_list(ll1.head)
#
# ll2.append(5)
# ll2.append(6)
# ll2.append(4)
# LinkedList.print_linked_list(ll2.head)

# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(2)
# ll.append(1)
# ll.append(2)
# ll.append(0)
# ll.append(2)
# ll.append(2)
# LinkedList.print_linked_list(ll.sort_linked_list())

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
# LinkedList.print_linked_list(ll.remove_nth(2))
LinkedList.print_linked_list(ll.rotat_linked_list(2))

