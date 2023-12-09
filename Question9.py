class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    def merge_linked_lists(self, linked_list2):
        linked_list_merged = LinkedList()
        linked_list_merged.head = self.merge_lists(self.head, linked_list2.head)
        return linked_list_merged
    def merge_lists(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.data < node2.data:
            result = node1
            result.next = self.merge_lists(node1.next, node2)
        else:
            result = node2
            result.next = self.merge_lists(node1, node2.next)
        return result
    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
linked_list1 = LinkedList()
n = int(input("Enter How Many Element in List1: "))
for i in range(n):
    data = int(input("Enter Element : "))
    linked_list1.insert(data)
linked_list2 = LinkedList()
n = int(input("Enter How Many Element in List2: "))
for i in range(n):
    data2 = int(input("Enter Element : "))
    linked_list2.insert(data2)
linked_list_merged = linked_list1.merge_linked_lists(linked_list2)
print("After merging the list is : ")
linked_list_merged.print_linked_list()
