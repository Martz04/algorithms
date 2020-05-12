import unittest
from linked_list import Node

def palindrome_list(head):
    #calculate middle of list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = slow.next.next
    
    #reverse second half
    mid = slow
    prev = mid
    cur = mid.next
    while cur:
        nxt = cur.next
        
        cur.next = prev
        prev = cur
        cur = nxt
    
    #compare both halves
    cur = head
    backwards = prev
    is_palindrome = True
    
    while cur is not mid and backwards is not mid:
        if cur.data != backwards.data:
            is_palindrome = False
        cur = cur.next
        backwards = backwards.next
    
    if cur is not mid or backwards is not mid:
        is_palindrome = False

    #revert reverse
    end = None
    tail = prev
    while tail is not mid:
        nxt = tail.next

        tail.next = end
        end = tail
        tail = nxt
    
    mid.next = end
    cur = head
    _str = ''
    while cur:
        _str += '{}->'.format(cur.data)
        cur = cur.next
    print(_str)
    return is_palindrome
    

class TestPalindromeList(unittest.TestCase):
    
    def test_ok(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(2)

        self.assertEqual(True, palindrome_list(head))

    def test_bad(self):
        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(6)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(2)

        self.assertEqual(False, palindrome_list(head))

if __name__ == "__main__":
    unittest.main()