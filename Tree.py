"""

"""


class TreeNode:

    def __init__(self, val, designation=None):
        self.val = val
        self.children = []
        self.parent = None
        # Its not default only for an exercise.
        self.designation = designation

    def addChild(self, child):
        # As the child node should have a parent, hence 'self' is used as the parent.
        child.parent = self
        self.children.append(child)

    def printTree(self, kywrd=None, limit=-1):
        # next 3 conditions for manangemnt example only. Else is default.
        if (kywrd == 'name'):
            suffix = self.val
        elif(kywrd == 'designation'):
            suffix = self.designation
        elif(kywrd == 'both'):
            suffix = f"{self.val} ({self.designation})"
        else:
            suffix = self.val

        lev = self.getLevel()
        if(limit >= 0 and lev > limit):
            return

        # Calculating space counts based on the node level.
        spaces = " "*lev*4

        # Checking if a node has a parent to give appropriate prefix.
        if self.parent:
            prefix = spaces+'>>|'
        else:
            prefix = ""

        # Print the current value of the TreeNode.
        print(prefix+" "+suffix)

        # Check if this particular node has any children.
        # Its as same as  if len(self.children)>0:
        if self.children:
            # If the node has children then iterate over each children.
            for child in self.children:
                child.printTree(kywrd, limit)

        # Recursive Fn to get the level of each Tree Node.

    def getLevel(self):
        # Counter to store level count.
        level = 0
        # Initial node is the parent of the node whose level is to found.
        p = self.parent
        # Iterate until a node's parent is 'None'.
        while(p):
            # Increase once as if it enters the loop then atleast one parent is present.
            level += 1
            # Change the node  to become its node.
            p = p.parent
        return level


def exampleTree():
    root = TreeNode("Companies")

    a = TreeNode("Sony")
    a.addChild(TreeNode(("PS1")))
    a.addChild(TreeNode(("PS2")))
    a.addChild(TreeNode(("PSP")))
    a.addChild(TreeNode(("PS3")))
    a.addChild(TreeNode(("PS4")))
    a.addChild(TreeNode(("PS5")))

    b = TreeNode("Microsoft")
    b.addChild(TreeNode(("Xbox")))
    b.addChild(TreeNode(("Xbox One")))
    b.addChild(TreeNode(("Xbox 360")))
    b.addChild(TreeNode(("Xbox X")))

    c = TreeNode("Nintendo")
    c.addChild(TreeNode(("Wii")))
    c.addChild(TreeNode(("Switch")))

    root.addChild(a)
    root.addChild(b)
    root.addChild(c)

    return root


def exampleMngmntTree():

    root = TreeNode("Aarav", "CEO")

    c = TreeNode("John", "Infrastructure Head")
    c.addChild(TreeNode("Dhaval", "Cloud Manager"))
    c.addChild(TreeNode("Stephan", "App Manager"))

    a = TreeNode("Hailey", "CTO")
    a.addChild(c)
    a.addChild(TreeNode("Ali", "Application Head"))

    b = TreeNode("Samantha", "HR Head")
    b.addChild(TreeNode("Leslie", "Recruitment Head"))
    b.addChild(TreeNode("Singh", "Policy Manager"))

    root.addChild(a)
    root.addChild(b)

    return root


def exampleLocation():
    root = TreeNode("Global")

    a = TreeNode("Gujarat")
    a.addChild(TreeNode("Ahmedabad"))
    a.addChild(TreeNode("Baroda"))

    b = TreeNode("Karnataka")
    b.addChild(TreeNode("Bengaluru"))
    b.addChild(TreeNode("Mysuru"))

    c = TreeNode("New Jersey")
    c.addChild(TreeNode("Princeton"))
    c.addChild(TreeNode("Trenton"))

    d = TreeNode("California")
    d.addChild(TreeNode("San Francisco"))
    d.addChild(TreeNode("Mountain View"))
    d.addChild(TreeNode("Palo Alto"))

    e = TreeNode("India")
    f = TreeNode("USA")

    e.addChild(a)
    e.addChild(b)
    f.addChild(c)
    f.addChild(d)
    root.addChild(e)
    root.addChild(f)

    return root


if __name__ == '__main__':
    companies = exampleTree()
    companies.printTree()

    root_node = exampleMngmntTree()
    root_node.printTree("name")
    root_node.printTree("designation")
    root_node.printTree("both")

    locations = exampleLocation()
    locations.printTree(limit=1)
    locations.printTree(limit=2)
    locations.printTree(limit=3)
