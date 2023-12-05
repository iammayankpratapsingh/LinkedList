class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = node
        node.next = head
    return head
def print_list(head):
    current = head
    while True:
        print(current.data, end=" ")
        current = current.next
        if current == head:
            break
def detect_remove_loop(head):
    tortoise = hare = head
    while True:
        if hare is None or hare.next is None:
            return None
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            break
    tortoise = head
    while tortoise.next != hare.next:
        tortoise = tortoise.next
        hare = hare.next
    hare.next = None
def menu_driven_program():
    head = None
    while True:
        print("\nMenu:")
        print("1. Insert node into the circular linked list")
        print("2. Detect and remove loop in the circular linked list")
        print("3. Print the circular linked list")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data: "))
            head = insert(head, data)
        elif choice == 2:
            detect_remove_loop(head)
        elif choice == 3:
            print_list(head)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu_driven_program()
