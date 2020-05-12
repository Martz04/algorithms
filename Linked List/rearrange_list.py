import unittest
from linked_list import Node

def reorder(head):
    # Get the half of the list
    if (head is None):
        return ""
    
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    # reverse the second half
    mid_pointer = slow
    prev = None
    cur = slow
    while cur is not None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    # while the left is not the same as the right pick a node 
    s, p, q = head, head.next, prev
    counter = 1
    while p is not mid_pointer or q is not mid_pointer:
        if counter % 2 == 0: #take from p
            s.next = p
            s = p
            p = p.next
        else:
            s.next = q
            s = q
            q = q.next
        counter += 1
    s.next = mid_pointer
    s.next.next = None

    cur = head
    response = ""
    while cur is not None:
        response += "{}->".format(cur.data)
        cur = cur.next
    return response

class TestProblem(unittest.TestCase):

    def test_one(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(8)
        head.next.next.next.next = Node(10)
        head.next.next.next.next.next = Node(12)
        self.assertEqual("2->12->4->10->6->8->", reorder(head))


if __name__ == "__main__":
    unittest.main()