'''
Implement hash table where collisions are handled using linear probing.
We learnt about linear probing in the video tutorial.
Take the hash table implementation that uses chaining and modify methods to use linear probing.
Keep MAX size of arr in hashtable as 10.
'''

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
            
        return h%self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h]:
            element = self.arr[h]
            for i in range(self.MAX):
                if element:
                    if element[0] == key:
                        self.arr[h] = (key, val)
                        return
                    else:
                        if h < self.MAX -1:
                            h += 1
                        else:
                            h = 0
                        if not self.arr[h]:
                            self.arr[h] = (key, val)
                            return
                        element = self.arr[h]
            
            raise Exception("Maximal Hash")
        else:
            self.arr[h] = (key, val)
        
    def __getitem__(self, key):
        h = self.get_hash(key)
       
        element = self.arr[h]
        while element:
            if element:
                if element[0] == key:
                    return self.arr[h][1]
                else:
                    if h < self.MAX -1:
                        h += 1
                    else:
                        h = 0
                    element = self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        
        element = self.arr[h]
        while element:
            if element:
                if element[0] == key:
                    self.arr[h] = None
                    break
                else:
                    if h < self.MAX -1:
                        h += 1
                    else:
                        h = 0
                    element = self.arr[h]
    
    
t = HashTable()
t["march 6"] = 10
t["march 6"] = 17
t["march 17"] = 28
t["march 17"] = 22
t["march 7"] = 22
t["march 8"] = 22
t["march 9"] = 22
t["march 10"] = 22
t["march 11"] = 22
t["march 12"] = 22
t["march 13"] = 22
t["march 14"] = 22

print(t.arr)
# print(t["march 14"])
# del t["march 17"]
# print(t.arr)