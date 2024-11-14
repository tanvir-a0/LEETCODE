class MyHashSet:

    def __init__(self):
        self.hash = []
        

    def add(self, key: int) -> None:
        self.hash.append(key)
        #print("added ", key, " hash: ", self.hash)

    def remove(self, key: int) -> None:
        while key in self.hash:
            self.hash.remove(key)
        #print("removed ", key, " hash: ", self.hash)

    def contains(self, key: int) -> bool:
        #print("conatin check ", key, " hash: ", self.hash)
        if key in self.hash:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
