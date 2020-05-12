import unittest
from binary_search_tree import BST

class BstProperty(unittest.TestCase):
    
    def test_one(self):
        bst = BST(7)
        bst.insert(3)
        bst.insert(10)
        bst.insert(5)
        bst.insert(1)
        bst.insert(8)
        bst.insert(9)
        bst.insert(2)

        self.assertEqual([1, 2, 3, 5, 7, 8, 9, 10], bst.inorder_traversal())

if __name__ == "__main__":
    unittest.main()