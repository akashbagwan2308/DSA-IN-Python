
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None]*self.max

    def get_hash(self,key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.max
    def __setitem__(self,key,val):
       h = self.get_hash(key)
       self.arr[h]=val
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h]= None




if __name__ == '__main__':
    h = HashTable()
    print(h.get_hash('march 6'))
    h['march 6'] = 302
    h['march 11'] = 22
    del h['march 11']
    print(h['march 11'])

