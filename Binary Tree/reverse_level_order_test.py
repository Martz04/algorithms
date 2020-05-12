from binary_tree import Node, BinaryTree
import unittest

class TestReverseLevelOrder(unittest.TestCase):

    def setUp(self):
        root = Node(1)
        self.tree = BinaryTree(root)
        self.tree.root.left = Node(2)
        self.tree.root.right = Node(3)
        self.tree.root.left.left = Node(4)
        self.tree.root.left.right = Node(5)

    def test_one(self):
        self.assertEqual("4 5 2 3 1 ", self.tree.reverse_level_order(self.tree.root))

    def test_height(self):
        self.assertEqual(2, self.tree.height(self.tree.root))

    def test_size(self):
        self.assertEqual(5, self.tree.size(self.tree.root))


if __name__ == "__main__":
    unittest.main()        