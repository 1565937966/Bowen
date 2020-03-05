from NodeAndList import SingleLine

class Node():
    def __init__(self, data):
        self.item = data
        self.next = None
        self.pre = None


class DoubleLine(SingleLine):
    def __init__(self):
        super().__init__()

    def add(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node
        node.next.pre = node

    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            while True:
                if current.next is None:
                    current.next = node
                    node.pre = current
                    break
                else:
                    current = current.next

    def insert(self, pos, item):
        current = self._head
        node = Node(item)
        counter = 0
        while counter < pos-1:
            counter += 1
            current = current.next
        temp = current.next
        current.next = node
        node.next = temp
        node.pre = current
        temp.pre = node
    '''
    def is_empty(self):

        if self.__head is None:
            return True
        else:
            return False
    '''


if __name__ == "__main__":
    double = DoubleLine()
    # print(double.is_empty())
    double.append(2)
    double.append(3)
    double.insert(1, 5)
    double.travel()
