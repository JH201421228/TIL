class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_node(self, prev_node, node_to_delete):
        if not prev_node:
            self.head = node_to_delete.next
        else:
            prev_node.next = node_to_delete.next

    def insert_after(self, prev_node, data):
        new_node = Node(data)
        if not prev_node:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return ''.join(result)

word = input()
cursor = len(word)
linked_list = LinkedList()
for char in word:
    linked_list.append(char)

for i in range(int(input())):
    input_keys = input().split()

    if input_keys[0] == 'L':
        if cursor != 0:
            cursor -= 1

    elif input_keys[0] == 'D':
        if cursor != len(word):
            cursor += 1

    elif input_keys[0] == 'B':
        if cursor != 0:
            node_to_delete = linked_list.head
            prev_node = None
            for _ in range(cursor):
                prev_node = node_to_delete
                node_to_delete = node_to_delete.next
            linked_list.delete_node(prev_node, node_to_delete)
            cursor -= 1

    else:
        linked_list.insert_after(linked_list.head, input_keys[1])
        cursor += 1

print(linked_list.display())
