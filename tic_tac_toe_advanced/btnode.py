"""
Module for Node class.
"""

class Node:
    """
    Represents a node in BT.
    """
    def __init__(self, value, left=None, right=None):
        """
        Node initialisation.
        """
        self.value = value
        self.left = left
        self.right = right
