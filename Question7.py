class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
def menu():
    print("\nDouble Linked List Menu:")
    print("1. Append to List")
    print("2. Print List")
    print("3. Find Middle Element")
    print("4. Exit")
dll = DoubleLinkedList()
while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to append: "))
        dll.append(data)
    elif choice == 2:
        dll.print_list()
    elif choice == 3:
        middle = dll.find_middle()
        if middle:
            print(f"Middle element is: {middle}")
        else:
            print("The list is empty.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
