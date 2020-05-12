class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self._insert_helper(self.root, new_val)

    def _insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self._insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self._insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self._search_helper(self.root, find_val)

    def _search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self._search_helper(current.right, find_val)
            else:
                return self._search_helper(current.left, find_val)

    def inorder_traversal(self):
        '''In-order traversal returns a list of the nodes in sorted order'''
        return self._inorder_helper(self.root, [])

    def _inorder_helper(self, current, paths):
        if current:  
            paths = self._inorder_helper(current.left, paths)
            paths.append(current.data)
            paths = self._inorder_helper(current.right, paths)

        return paths
        