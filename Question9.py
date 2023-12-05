class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()
def merge_lists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.data < list2.data:
        list1.next = merge_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_lists(list1, list2.next)
        return list2
def main():
    list1 = LinkedList()
    list2 = LinkedList()
    print("Enter list1:")
    while True:
        inp = input()
        if inp:
            list1.push(int(inp))
        else:
            break
    print("Enter list2:")
    while True:
        inp = input()
        if inp:
            list2.push(int(inp))
        else:
            break
    print("Merged list:")
    merged_list = merge_lists(list1.head, list2.head)
    merged_list.print_list()
if __name__ == "__main__":
    main()
