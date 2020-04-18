import unittest
from linked_list import Node, LinkedList

def length_of_cycle(linkedList):
    slow, fast = linkedList.head, linkedList.head
    cross_pointer = None
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            cross_pointer = slow
            break
    if cross_pointer is not None:
        count = 1
        len_pointer = cross_pointer.next
        while len_pointer != cross_pointer:
            count += 1
            len_pointer = len_pointer.next
        return count
    else:
        return 0 

class TestCyclic(unittest.TestCase):

    def test_length(self):
        '''Given the head of a linked list with a cycle
            find the length of the cycle'''
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        head.next.next.next.next.next.next = head.next.next
        llist = LinkedList(head)

        self.assertEqual(4, length_of_cycle(llist))

if __name__ == "__main__":
    unittest.main()