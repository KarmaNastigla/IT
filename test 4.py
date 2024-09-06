class Node:             # Класс узла двусвязного списка.
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:    # Класс двусвязного списка.
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, data):   # Добавляет значение в конец списка.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def pop(self):          # Удаляет значение с конца списка.
        if self.tail is None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return temp.data
    def shift(self):         # Удаляет значение в начале списка.
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return temp.data
    def unshift(self, data):    # Добавляет значение в начало списка.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

dll = DoublyLinkedList()
dll.push(20)
dll.push(30)
dll.push(40)

print(dll.pop())
print(dll.shift())
dll.unshift(40)
print(dll.head.data)