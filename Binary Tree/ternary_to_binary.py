import unittest
from binary_tree import Node, BinaryTree

def convertStringToBinary(string):
    tree, _ = solution(string)
    return inorder(tree)


def solution(string, index = 0):
    if index >= len(string) - 1:
        return Node(string[-1]), len(string)
    
    current = string[index]
    next = string[index + 1]
    if next == ':':
        return Node(current), index + 2

    if next == '?':
        root = Node(current)
        (node_left, next_index) = solution(string, index + 2)
        (node_right, other_next) = solution(string, next_index)    
        root.left = node_left
        root.right = node_right
        return root, other_next
    

def inorder(tree):
    current = tree
    if current is None:
        return 

    if isLeaf(current):
        return current.data

    values = []
    values.append(current.data)
    values.append(inorder(current.left))
    values.append(inorder(current.right))

    return " ".join(values)


def isLeaf(node):
    return True if node.left is None and node.right is None else False

class TernaryToBinaryTree(unittest.TestCase):
    '''Given a string that contains ternary expressions. 
        The expressions may be nested, task is convert the given ternary expression to a binary Tree.
        Input :  string expression =   a?b:c 
        Output :        a
                      /  \
                     b    c
        The output should print the BinaryTree in preorder format             
    '''                 

    def test_one(self):
        input = "a?b:c"
        output = "a b c"
        self.assertEqual(output, convertStringToBinary(input))

    def test_two(self):
        input = "a?b?c:d:e"
        output = "a b c d e"
        self.assertEqual(output, convertStringToBinary(input))

if __name__ == "__main__":
    unittest.main()