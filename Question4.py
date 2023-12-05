class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
def print_list(head):
    if head is None:
        print("List is empty!")
        return
    node = head
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("NULL")
def main():
    head = None
    while True:
        print("------- MENU -------")
        print("1. Create List")
        print("2. Reverse List")
        print("3. Print List")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to add: "))
            node = Node(data)
            if head is None:
                head = node
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = node
        elif choice == 2:
            head = reverse_list(head)
        elif choice == 3:
            print_list(head)
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()
