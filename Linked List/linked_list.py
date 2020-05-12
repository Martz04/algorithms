import pdb

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_two_lists(list1, list2):
    p = list1.head
    q = list2.head
    
    s = None
    s_head = None

    # point s to the smaller of both heads
    if p.data < q.data:
        s = p
        p = s.next
    else:
        s = q
        q = s.next

    s_head = s
    #pdb.set_trace()
    while p or q:  
        if p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = p.next
            else:
                s.next = q
                s = q
                q = q.next
        elif p is None:
            s.next = q
            s = q
            q = q.next
        else:
            s.next = p
            s = p
            p = p.next
    return s_head


class LinkedList(object):

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 1:
            raise TypeError('Only one argument is allowed')
        if len(args) > 0:        
            self.head = Node(args[0])
        else:
            self.head = kwargs['node']


    def append(self, value):
        n = Node(value)
        current = self.head
        
        while current.next:
            current = current.next
        current.next = n


    def print_list(self):
        current = self.head
        output = ''
        while current:
            output += "{}->".format(current.data)
            current = current.next
        print(output)


    def remove_duplicates(self):
        cur = self.head
        prev = None
        seen_values = dict()

        while cur:
            if cur.data in seen_values:
                prev.next = cur.next
                cur = None
            else:
                seen_values[cur.data] = 1
                prev = cur
            cur = prev.next


    def len_recursive(self):
        cur = self.head
        def reduce(node):
            if node is None:
                return 0
            return 1 + reduce(node.next)
        return reduce(cur)


    def print_nth_from_last(self, n):
        total_len = self.len_recursive()

        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return