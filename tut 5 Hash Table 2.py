# Collision Handling
# Linear chaining and linear probaing


class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.max
    def __setitem__(self,key,val):
       h = self.get_hash(key)
       found = False
       for idx,element in enumerate(self.arr[h]):
           if len(element) ==2 and element[0]==key:
               self.arr[h][idx]=(key,val)
               found = True
       if not found:
           self.arr[h].append((key,val))
    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index,kv in enumerate(self.arr[h]):
            if kv[0]== key:
                del self.arr[h][index]


if __name__ == '__main__':
    h = HashTable()
    h['march 6']=120
    h['march 8']=67
    h['march 9']=4
    h['march 17']=459

    print(h['march 17'])
    del h['march 6']
    print(h.arr)