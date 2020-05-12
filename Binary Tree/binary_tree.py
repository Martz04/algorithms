class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, node):
        self.root = node

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def reverse_level_order(self, start):
        queue = []
        stack = []
        queue.append(start)
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            stack.append(current)
        
        _str = ''   
        while len(stack) > 0:
            _str += str(stack.pop(-1).value) + " "
        return _str

    def height(self, start):
        if start is None:
            return -1

        left_h = self.height(start.left)
        right_h = self.height(start.right)
        return 1 + max(left_h, right_h)

    def size(self, start):
        stack = []
        count = 0
        if start:
            count += 1
            stack.append(start)
            while len(stack) > 0:
                current = stack.pop()
                if current.left:
                    stack.append(current.left)
                    count += 1
                if current.right:
                    stack.append(current.right)
                    count += 1
        return count