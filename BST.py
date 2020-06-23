"""
My implementation of a Binary Search Tree with its 3 different types of traversals. 
"""


class BSTNode:
    def __init__(self, value):
        self.left = None
        self.val = value
        self.right = None

    def addChild(self, child):
        # Dont do anything if value already exist(set is implemented using BST).
        if (child == self.val):
            return
        if (child < self.val):
            # add data in left subtree
            # Check if you are the leaf
            if self.left:  # Enters if not a leaf node.
                # Recursive method makes it very easy.
                self.left.addChild(child)
            else:  # Enters if its a leaf node.
                # Adds a new BSTNode with 'child' as value.
                self.left = BSTNode(child)
        else:
            # add data in right subtree
            if self.right:  # Enters if not a leaf node.
                self.right.addChild(child)
            else:  # Enters if its a leaf node.
                # Adds a new BSTNode with 'child' as value.
                self.right = BSTNode(child)

    def inorder_recursive(self):
        # It will contain the result
        elements = []

        # first visit left subtree
        if self.left:
            # here '+' only works due to recursive activity.
            elements += self.left.inorder_recursive()

        # Then visit root nodes
        elements.append(self.val)

        # Lastly visit right subtree
        if self.right:
            elements += self.right.inorder_recursive()

        return elements

    def preorder_recursive(self):
        # It will contain the result
        elements = []

        # first visit root nodes
        elements.append(self.val)

        # Then visit left subtree
        if self.left:
            # here '+' only works due to recursive activity.
            elements += self.left.preorder_recursive()

        # Lastly visit right subtree
        if self.right:
            elements += self.right.preorder_recursive()

        return elements

    def postorder_recursive(self):
        # It will contain the result
        elements = []

        # first visit left subtree
        if self.left:
            # here '+' only works due to recursive activity.
            elements += self.left.postorder_recursive()

        # Then visit right subtree
        if self.right:
            elements += self.right.postorder_recursive()

        # Lastly visit root nodes
        elements.append(self.val)

        return elements


def buildTree(nums):  # Helper Fn to build a BST from a list of numbers
    root = BSTNode(nums[0])
    for i in range(1, len(nums)):
        root.addChild(nums[i])
    return root


if __name__ == '__main__':  # main() Fn
    nums = [21, 41, 1, 20, 9, 12, 85, 12]
    r = buildTree(nums)
    print(f"\n In-order Traversal Results: {r.inorder_recursive()}")
    print(f"\n Pre-order Traversal Results: {r.preorder_recursive()}")
    print(f"\n Post-order Traversal Results: {r.postorder_recursive()}\n")
