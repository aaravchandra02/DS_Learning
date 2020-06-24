"""
My implementation of a Binary Search Tree with its 3 different types of traversals.
"""
# To find System properties
import sys


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

    def findMin(self):
        # First element with no left is the smallest element in the BST.
        if self.left:
            return self.left.findMin()
        return self.val

    def findMax(self):
        # First element with no right is the largest element in the BST.
        if self.right:
            return self.right.findMax()
        return self.val

    def calculateSum(self):
        # Traversed and added every element and finally returned it.
        summation = 0
        if self.left:
            summation += self.left.calculateSum()
        summation += self.val
        if self.right:
            summation += self.right.calculateSum()
        return summation
        """
        def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
        """

    def searchTree(self, ele):

        if (self.val == ele):
            return True
        if (ele < self.val):
            if(self.left):  # as tree node might not have a left, meaning element not present
                return self.left.searchTree(ele)
            else:
                return False
        if (ele > self.val):
            if(self.right):  # as tree node might not have a right, meaning element not present
                return self.right.searchTree(ele)
            else:
                return False

    # Either put min node from left subtree or max node from right subtree.
    def deleteNode(self, ele):

        # Traversing the tree to get the node that needs to be deleted

        if ele < self.val:  # If element is < current
            if self.left:  # If left subtree is present, See it.
                self.left = self.left.deleteNode(ele)  # Copying
        elif ele > self.val:  # If element is > current
            if self.right:  # If right subtree is present, See it.
                self.right = self.right.deleteNode(ele)
        else:  # When ELement is found
            if self.left is None and self.right is None:  # if its a leaf node
                return None
            elif (self.left):  # If its only has left subtree
                return self.left  # copying it by skipping the choosen element
            elif (self.right):  # If its only has right subtree
                return self.right
            else:  # When its having both subtrees
                min_val = self.left.find_max()  # could also be min of its right tree
                self.data = min_val  # Changing the current nodes value
                # deleting the OG changed element
                self.right = self.right.deleteNode(min_val)
        return self  # Returning the main tree with deleted node.


def buildTree(nums):  # Helper Fn to build a BST from a list of numbers
    root = BSTNode(nums[0])
    for i in range(1, len(nums)):
        root.addChild(nums[i])
    return root


if __name__ == '__main__':  # main() Fn
    nums = [21, 41, 1, 20, 9, 12, 85, 17]
    r = buildTree(nums)
    print(f"\n In-order Traversal Results: {r.inorder_recursive()}")
    print(f"\n Pre-order Traversal Results: {r.preorder_recursive()}")
    print(f"\n Post-order Traversal Results: {r.postorder_recursive()}")
    print(f"\n Minimum Element in the Tree: {r.findMin()}")
    print(f"\n Maximum Element in the Tree: {r.findMax()}")
    print(f"\n Summation of all elements: {r.calculateSum()}")
    # ns = int(input("\n Enter the element that you want to search in the tree: "))
    ns = 1
    print(f"\n Search Result for element {ns} : {r.searchTree(ns)}")
    # nd = int(input("\n Enter the element that you want to delete in the tree: "))
    nd = 1
    w = (r.deleteNode(nd))
    print(f"\n In-order Traversal Results: {w.inorder_recursive()}")
