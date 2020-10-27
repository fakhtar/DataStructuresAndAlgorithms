class _listitem:
    def __init__(self, prev, next, val):
        self.next = next
        self.prev = prev
        self.val = val


class my_queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def enqueue(self,val):
        if val == None:
            raise ValueError('Cannot enqueue None value.')
        if self.size == 0:
            self.first = self.last = _listitem(None,None,val)
            self.size += 1
        else:
            self.last = _listitem(None,self.last,val)
            self.size += 1
            self.last.next.prev = self.last
        return self.last.val
    def dequeue(self):
        if self.size == 0:
            raise ValueError('Cannot dequeue an empty que.')
        elif self.size == 1:
            retval = self.first.val
            self.first = None
            self.last = None
            self.size -= 1
        else:
            retval = self.first.val
            self.first = self.first.prev
            self.first.next = None
            self.size -= 1
        return retval
    def front(self):
        if self.size == 0:
            raise ValueError('Cannot get front from an empty que.')
        else:
            return self.first.val
    def back(self):
        if self.size == 0:
            raise ValueError('Cannot get back from an empty que.')
        else:
            return self.last.val
    def get_list(self):
        list_representation = []
        curr_node = self.last
        if curr_node == None:
            return []
        while True:
            list_representation.append(curr_node.val)
            if curr_node.next != None:
                curr_node = curr_node.next
                continue
            if curr_node.next == None:
                #list_representation.append(curr_node.val)
                break
        return list_representation

class naieveQueue:
    def __init__(self):
        self.items = []
    def enqueue(self,val):
        if val == None:
            raise ValueError('Cannot enqueue None value.')
        self.items.insert(0,val)
        return val
    def dequeue(self):
        if len(self.items) == 0:
            raise ValueError('Cannot dequeue an empty que.')
        retval = self.items[-1]
        self.items.pop()
        return retval
    def front(self):
        if len(self.items) == 0:
            raise ValueError('Cannot front an empty que.')
        return self.items[-1]
    def back(self):
        if len(self.items) == 0:
            raise ValueError('Cannot back an empty que.')
        return self.items[0]
    def get_list(self):
        return self.items

if __name__ == '__main__':
    test_queue = my_queue()
    my_naieve_queue = naieveQueue()
    test_queue.enqueue(20)
    my_naieve_queue.enqueue(20)
    test_queue.dequeue()
    my_naieve_queue.dequeue()
    test_queue.get_list()
    my_naieve_queue.get_list()