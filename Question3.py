class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            new_node.next = self.head
            self.head = new_node
            tmp.next = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            new_node.next = self.head
            tmp.next = new_node
    def delete_at_beginning(self):
        if self.is_empty():
            print("List is empty!")
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                tmp = self.head
                while tmp.next != self.head:
                    tmp = tmp.next
                tmp.next = self.head.next
                self.head = tmp.next
    def delete_at_end(self):
        if self.is_empty():
            print("List is empty!")
        else:
            if self.head.next == self.head:
                self.head = None
            else:
                prev = None
                tmp = self.head
                while tmp.next != self.head:
                    prev = tmp
                    tmp = tmp.next
                prev.next = self.head
    def traverse(self):
        if self.is_empty():
            print("List is empty!")
        else:
            tmp = self.head
            while tmp:
                print(tmp.data, end=" -> ")
                tmp = tmp.next
                if tmp == self.head:
                    break
            print("NULL")
def main():
    circular_list = CircularLinkedList()
    while True:
        print("------- MENU -------")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete at Beginning")
        print("4. Delete at End")
        print("5. Traverse")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert: "))
            circular_list.insert_at_beginning(data)
        elif choice == 2:
            data = int(input("Enter data to insert: "))
            circular_list.insert_at_end(data)
        elif choice == 3:
            circular_list.delete_at_beginning()
        elif choice == 4:
            circular_list.delete_at_end()
        elif choice == 5:
            circular_list.traverse()
        elif choice == 6:
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
