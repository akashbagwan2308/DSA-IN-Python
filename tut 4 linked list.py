class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            suffix = ''
            if itr.next:
                suffix = '-->'
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def insert(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    root = LinkedList()
    # root.insert_at_begining(5)
    # root.insert_at_begining(15)
    # root.insert_at_begining(10)
    # root.insert_at_end(5225)
    # root.insert_at_end(55)
    # root.insert_at_end(25)
    # root.insert_at(2,2555)
    # root.insert_at(1,40)
    # root.remove_at(3)
    l = [14, 23, 25, 28, 27, 15, 8]
    root.insert(l)
    root.print()
    print(root.get_length())
