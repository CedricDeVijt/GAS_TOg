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

class Node():
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class MyStack():
    def __init__(self):
        self.top = None 
    
    def isEmpty(self):
        return (self.top==None)

    def getTop(self):
        if self.top!=None:
            return (self.top.value, self.top!=None)
        return (self.top, self.top!=None)

    def push(self,item): 
        node = Node(item) 
        if(self.top == None):
            self.top = node
        else:
            node.next = self.top 
            self.top = node
        return True

    def pop(self):
        if(self.top == None):
            return (None, False)
        else:
            node = self.top 
            self.top = node.next 
            node.next = None  
            item = node.item   
            del node
            return (item, self.top!=None)

    def save(self):
        l = []
        tgt = self.top
        while tgt!=None:
            l.insert(0, tgt.item)
            tgt = tgt.next
        return l

    def load(self, l):
        self.__init__()
        for elem in l:
            self.push(elem)

class StackTable(MyStack):
    def __init__(self):
        super().__init__()
    
    #Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty

        preconditions: None
        postconditions: Returns True if the table is empty
        """
        return self.isEmpty()

    #Inserts a TreeItem to the table
    def tableInsert(self, item):
        """
        Inserts a TreeItem to the table

        TreeItem is of type twoThreeNode

        preconditions: None
        postconditions: The treeItem gets inserted to the table
        """
        return self.push(item)

    #Retrieves an item from the table
    def tableRetrieve(self):
        """
        Retrieves an item from the table

        preconditions: None
        postconditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        return self.getTop()

        
    #Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table

        item is the target for deletion

        preconditions: None
        postconditions: The given item gets deleted from the table
        """
        return self.pop()

    def createTableItem(self, key, val):
        return Item(key, val)