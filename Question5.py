class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(head, data):
    if not head:
        return Node(data)
    last = head
    while last.next:
        last = last.next
    last.next = Node(data)
    return head
def is_palindrome(head):
    if not head:
        return True
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_half = reverse(slow)
    is_palindrome = True
    while second_half and is_palindrome:
        if head.data != second_half.data:
            is_palindrome = False
        head = head.next
        second_half = second_half.next
    return is_palindrome
def reverse(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev
head = None
while True:
    try:
        data = int(input("Enter a number (0 to stop): "))
        if data == 0:
            break
        head = insert(head, data)
    except ValueError:
        print("Please enter a valid number.")
result = is_palindrome(head)
if result:
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
