class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
    def reverse(self):
        temp = None
        node = self.head
        while node:
            temp = node.prev
            node.prev = node.next
            node.next = temp
            node = node.prev
        if temp:
            self.head = temp.prev
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' ')
            node = node.next
        print()
def menu_driven():
    dll = DoublyLinkedList()
    while True:
        print("\n1. Insert")
        print("2. Reverse")
        print("3. Print List")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data to insert: "))
            dll.insert(data)
        elif choice == 2:
            dll.reverse()
        elif choice == 3:
            dll.print_list()
        elif choice == 4:
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    menu_driven()
