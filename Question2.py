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
    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next
    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
double_linked_list = DoubleLinkedList()
while True:
    print("\nDouble Linked List Operations : ")
    print("1. Append")
    print("2. Delete")
    print("3. Traverse")
    print("4. Quit")
    choice = input("Enter your choice : ")
    if choice == '1':
        data = input("Enter data to append : ")
        double_linked_list.append(data)
    elif choice == '2':
        key = input("Enter key to delete : ")
        double_linked_list.delete(key)
    elif choice == '3':
        double_linked_list.traverse()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again...")
