class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode(-1, -1) for _ in range(10000)] 

    def put(self, key: int, value: int) -> None:
        index = key % 10000
        cur = self.arr[index]
        while cur.next and cur.next.key != key:
            cur = cur.next
        
        if cur.next:
            cur.next.val = value
        else: 
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % 10000
        cur = self.arr[index]
        while cur and cur.key != key:
            cur = cur.next
        return cur.val if cur else -1

    def remove(self, key: int) -> None:
        index = key % 10000
        cur = self.arr[index]
        while cur.next and cur.next.key != key:
            cur = cur.next
        cur.next = cur.next.next if cur.next else None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)