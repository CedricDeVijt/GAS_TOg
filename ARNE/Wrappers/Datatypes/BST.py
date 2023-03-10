def createItem(key,val):
    return Item(key, val)

class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self) -> str:
        return "key: " + str(self.key) + ", val: " + str(self.val)

#Tree Node of Binary Search Tree
class BSTNode():
    #Initialisation Node
    def __init__(self, item = None) -> None:
        """
        Initialisation Node

        key is set to self.key, the default value is None
        value is set to self.value, the default value is None

        preconditions: None
        postconditions: A BSTNode is created
        """
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
    
    #Checks if the node is a leaf
    def isLeaf(self):
        """
        Checks if the node is a leaf

        preconditions: None
        postconditions: True if the node is a leaf, False if the node is not a leaf
        """
        return self.right==None and self.left==None
    
    #Checks if the node is empty
    def isEmpty(self):
        """
        Checks if the node is empty

        preconditions: None
        postconditions: True if the node is emtpy, False if the node is not empty
        """
        return self.item is None

    #Inserts an item to binary search Tree
    def searchTreeInsert(self, item):
        """
        Inserts a value to binary search Tree

        treeItem is a Binary Search Tree Node
        currentNode is the node that is being processed

        preconditions: There is a root
        postconditions: returns True if insertion worked
        """
        if self.item.key==item.key:
            return True
        elif self.item.key>item.key:
            if self.left is None:
                self.left = BSTNode(item)
                self.left.parent = self
                return True
            else:
                self.left.searchTreeInsert(item)
        else:
            if self.right is None:
                self.right = BSTNode(item)
                self.right.parent = self
                return True
            else:
                self.right.searchTreeInsert(item)
    
    def inorderTraverse(self, func):
        """
        Prints the Binary Search Tree inorder

        print variable is unused but needed for Inginious
        currentNode is the node that is being processed

        preconditions: There is a root
        postconditions: Prints the Binary Search Tree inorder
        """
        if self.left is not None:
            self.left.inorderTraverse(func)

        func(self.item)

        if self.right is not None:
            self.right.inorderTraverse(func)

    #Searches a value in a Binary Search Tree
    def searchTreeRetrieve(self, item):
        """
        Searches a value in a Binary Search Tree

        currentNode is the node that is being processed

        preconditions: The root is not empty
        postconditions: returns a tuple containing the value and a bool that is True when the value is found
        """
        if self.isEmpty():
            return None, False
        
        if self.item.key==item.key:
            return self, True

        if item.key<self.item.key and self.left is not None:
            return self.left.searchTreeRetrieve(item)
        elif item.key>self.item.key and self.right is not None:
            return self.right.searchTreeRetrieve(item)
        return None, False


        #Saves the contents of a Binary Search Tree
    def save(self):
        """
        Saves the contents of a Binary Search Tree
        
        currentNode is the node that is being processed

        preconditions: None
        postconditions: returns a dictionary describing the root, children and its items of a Binary Search Tree
        """
        d = {}
        d["root"] = self.item
        if not self.isLeaf():
            d["children"] = [None, None]
            if type(self.left)==BSTNode:
                if not self.left.isEmpty():
                    d["children"][0] = self.left.save()
            if type(self.right)==BSTNode:
                if not self.right.isEmpty():
                    d["children"][1] = self.right.save()
        return d
    
    def load(self, dictIn):
        """
        Loads a new binary search tree

        dictIn is a dictionary in the right format
        currentNode is the node that is being processed

        preconditions: None
        postconditions: Creates a new Binary Search Tree with the right elements
        """
        self.item = Item(dictIn["root"], "")
        if "children" in dictIn.keys():
            leftTree = dictIn["children"][0]
            rightTree = dictIn["children"][1]
            if type(leftTree)==dict:
                self.left = BSTNode()
                self.left.parent = self
                self.left.load(leftTree)
            else:
                self.left = leftTree
            if type(rightTree)==dict:
                self.right = BSTNode()
                self.right.parent = self
                self.right.load(rightTree)
            else:
                self.right = rightTree
    
#Binary Search Tree
class BST():
    #Initialisation of Binary Search Tree
    def __init__(self) -> None:
        """
        Initialisation of Binary Search Tree
        
        Preconditions: None
        Postconditions: An empty BST is created
        """
        self.root = BSTNode()
    
    #Checks if the Binary Search Tree is empty
    def isEmpty(self):
        """
        Checks if the Binary Search Tree is empty

        preconditions: None
        postconditions: True if the tree is emtpy, False if the tree is not empty
        """
        return self.root.isEmpty()
    
    #Inserts a value to binary search Tree
    def searchTreeInsert(self, item):
        """
        Inserts a value to binary search Tree

        treeItem is a Binary Search Tree Node

        preconditions: None
        postconditions: returns True if insertion worked
        """
        if self.isEmpty():
            self.root.item = item
            return True
        return self.root.searchTreeInsert(item)
    
    #Prints the Binary Search Tree inorder
    def inorderTraverse(self, func):
        """
        Prints the Binary Search Tree inorder

        print variable is unused but needed for Inginious

        preconditions: None
        postconditions: Prints the Binary Search Tree inorder
        """
        if self.root!=None:
            self.root.inorderTraverse(func)
    
    #Searches a value in a Binary Search Tree
    def searchTreeRetrieve(self, item):
        """
        Searches a value in a Binary Search Tree

        preconditions: None
        postconditions: returns a tuple containing the value and a bool that is True when the value is found
        """
        if self.root!=None:
            return self.root.searchTreeRetrieve(item)
        else:
            return None, False
    
    #Saves the contents of a Binary Search Tree
    def save(self):
        """
        Saves the contents of a Binary Search Tree

        preconditions: None
        postconditions: returns a dictionary describing the root, children and its items of a Binary Search Tree
        """
        if self.root!=None:
            return self.root.save()
        return {}

    #loads a new binary search tree
    def load(self, dictIn):
        """
        Loads a new binary search tree

        dictIn is a dictionary in the right format

        preconditions: None
        postconditions: Creates a new Binary Search Tree with the right elements
        """
        self.root = BSTNode()
        self.root.load(dictIn)
    
    #Deletes a node from the binary search tree
    def searchTreeDelete(self, item):
        """
        Deletes a node from the binary search tree
        
        value is the value of the node that needs to be deleted

        preconditions: None
        postconditions: returns True if the value is deleted from the tree
        """
        node, succes = self.searchTreeRetrieve(item)
        if succes:
            if node == self.root:
                self.root = BSTNode()
            else:
                self.deleteNode(node)
            return True
        return False
    #Deletes a node
    def deleteNode(self, node):
        """
        Deletes a node

        node is the node that needs to get deleted

        preconditions: the value has to be in the binary search tree
        postconditions: deletes a node from the binary search tree
        """
        #returns the node with the smallest value
        def getMinNode(n):
            """
            returns the node with the smallest value

            n is a node item

            preconditions: None
            postconditions: returns the node with the smallest value
            """
            min=n
            while min.left!=None:
                min=min.left
            return min
        #returns the amount of children a node has
        def childrenAmount(node):
            """
            returns the amount of children a node has

            node is the node that is being processed

            preconditions: None
            postconditions: returns the amount of children the given node has
            """
            amount = 0
            if node.left!=None: 
                amount+=1
            if node.right!=None:
                amount+=1
            return amount

        parent = node.parent
        children = childrenAmount(node)
        if node.isLeaf():
            if parent.left==node:
                parent.left=None
            else:
                parent.right=None
                
        if children==1:
            if node.left!=None:
                child = node.left
            else:
                child = node.right
            if parent.left==node:
                parent.left=child
            else:
                parent.right=child
            child.parent = parent

        if children==2:
            successor = getMinNode(node.right)
            node.value = successor.value
            self.deleteNode(successor)