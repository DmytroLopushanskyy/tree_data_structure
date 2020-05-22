"""
Module for LinkedBinaryTree
"""


class LinkedBinaryTree:
    """
    Represents a binary tree.
    """
    def __init__(self, root):
        """
        Tree initialisation.
        """
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """
        Inserts node as a left child.
        """
        if self.left_child is None:
            self.left_child = LinkedBinaryTree(new_node)
        else:
            tree = LinkedBinaryTree(new_node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, new_node):
        """
        Inserts node as a right child.
        """
        if self.right_child is None:
            self.right_child = LinkedBinaryTree(new_node)
        else:
            tree = LinkedBinaryTree(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_right_child(self):
        """
        Returns right child
        """
        return self.right_child

    def get_left_child(self):
        """
        Returns left child.
        """
        return self.left_child

    def set_root_val(self, obj):
        """
        Sets obj as a root value.
        """
        self.key = obj

    def get_root_val(self):
        """
        Returns a root value.
        """
        return self.key

    def preorder(self):
        """
        Preorder traversal.
        """
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        """
        Inorder traversal.
        """
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        """
        Postorder traversal.
        """
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()
        print(self.key)
