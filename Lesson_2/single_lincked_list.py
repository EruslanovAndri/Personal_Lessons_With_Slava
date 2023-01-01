class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}]->{self.next}"

class LinckedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

if __name__ == '__main__':

    linked_list = LinckedList()
    temp = Node(1)
    linked_list.head = temp
    for i in range(2,5):
        temp.next = None(i)
        temp = temp.next

