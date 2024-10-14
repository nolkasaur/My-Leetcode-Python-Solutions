# https://leetcode.com/problems/lru-cache/
# 572 ms, 79.40 MB

class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.previous = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap_cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0) # LRU dummy node on the left of the list, MRU dummy node on the right of the list
        self.left.next, self.right.previous = self.right, self.left

    def insert(self, node):
        previous, next = self.right.previous, self.right
        previous.next = next.previous = node
        node.previous, node.next = previous, next

    def remove(self, node):
        previous, next = node.previous, node.next
        previous.next, next.previous = next, previous

    def get(self, key: int) -> int:
        if key in self.hashmap_cache:
            self.remove(self.hashmap_cache[key])
            self.insert(self.hashmap_cache[key])
            return self.hashmap_cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap_cache:
            self.remove(self.hashmap_cache[key])
        self.hashmap_cache[key] = Node(key, value)
        self.insert(self.hashmap_cache[key])
        if len(self.hashmap_cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap_cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
