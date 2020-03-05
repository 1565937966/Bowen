class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLine:
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        if self._head is None:
            print("empty list")
        else:
            return False

    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            '''
            while current.next is not None:
                current = current.next
            '''
            while True:
                if current.next is None:
                    current.next = node
                    break
                else:
                    current = current.next
            # current.next = node

    def remove(self, data):
        current = self._head
        if current.item == data:
            if current.next is not None:
                self._head = current.next
                current = self._head
            else:
                self._head = None
        # pre = None
        while current.next is not None:
            if current.next.item == data:
                current.next = current.next.next
                # break  # because it doesn't have any information about current, so it have to use break to break the loop
            else:
                # pre = current
                current = current.next

    def add(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
        else:
            temp = self._head
            self._head = node
            # current = self._head
            node.next = temp

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

    def length(self):
        counter = 0
        if self._head is None:
            return counter
        else:
            current = self._head
            while current:
                current = current.next
                counter += 1
            return counter

    def travel(self):
        if self._head is None:
            print("No element in this list")
        else:
            current = self._head
            while current is not None:
                print(current.item, end=",")
                current = current.next

    def search(self, item):
        pass

    def reversed_print(self):
        current = self._head
        pre = None
        while current is not None:
            temp = current
            current = current.next
            temp.next = pre
            pre = temp
        while pre:
            print(pre.item)
            pre = pre.next



if __name__ == "__main__":

    List = SingleLine()
    # List.append(20)
    # List.append(30)
    List.append(10)
    List.append(20)
    List.append(30)
    # List.insert(2, 3)
    # List.insert(2, 20)
    # print(List.travel())
    # print(List.length())
    print(List.reversed_print())

    # List.remove(20)
    # print(List.travel())
    # List.remove(10)
    # print(List.travel())

'''
    List.add(8)
    List.insert(2, 5)
    print("Length is %d" % List.length())
    List.travel()
    List.remove()
    List.travel()
    print("Length is %d" % List.length())
    # print(List.is_empty())
    List = SingleLine()
    for i in range(0, 10):
        List.append(i)
    print("Length is %d" % List.length())
    List.travel()
    List.add(11)
    print("\nNew list: ")
    List.travel()
    List.insert(6, 20)
    print("\nInsert new list: ")
    List.travel()
    '''
