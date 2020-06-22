# Creating a Linked List
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    # Traversing the Linked List
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Inserting at the beginning of linked list
    def AtBegining(self, newdata):
        NewNode = Node(newdata)

    # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Inserting at the end of linked list
    # Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval=NewNode

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.AtBegining("Sun")
list1.AtEnd("Thu")
list1.listprint()
