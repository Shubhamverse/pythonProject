from array import *

ele = array('i')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begn(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            ele.append(current.data)
            # print(current.data, end=" ")
            current = current.next


a_llist = LinkedList()
n = int(input("How many elements would you like to add? "))
for i in range(n):
    data = int(input("Enter data items: "))
    node = Node(data)
    a_llist.insert_at_begn(node)


print("The Linked List: ", end=" ")
a_llist.display()
for i in range(n):
    print(ele[i], end=' ')