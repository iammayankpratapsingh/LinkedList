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
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
    def traverse(self):
        temp = self.head
        print("The Linked List : ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
linked_list = LinkedList()
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the value to insert : "))
        linked_list.insert(data)
    elif choice == 2:
        data = int(input("Enter the value to delete : "))
        linked_list.delete(data)
    elif choice == 3:
        linked_list.traverse()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
