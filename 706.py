class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        bucket_index = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            if k == key:
                self.buckets[bucket_index][i] = (key, value)
                return
        self.buckets[bucket_index].append((key, value))
    
    def get(self, key: int) -> int:
        bucket_index = self.hash(key)
        for k, v in self.buckets[bucket_index]:
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        bucket_index = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[bucket_index]):
            if k == key:
                del self.buckets[bucket_index][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
