# Question Description
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

# Constraints:

# 0 <= key, value <= 106
# At most 104 calls will be made to put, get, and remove.

# Solution
class ListNode:
    def __init__(self,key,value,next):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self,length=10000):
        self.length = length
        self.nodeList = [None for _ in range(self.length)]

    def hashKey(self,key):
        return hash(key)%self.length

    def put(self, key: int, value: int) -> None:
        keyForHash = self.hashKey(key)

        nodesHead = self.nodeList[keyForHash]
        if nodesHead == None:
            newNode = ListNode(key,value,self.nodeList[keyForHash])
            self.nodeList[keyForHash] = newNode
        else:
            while nodesHead:
                if nodesHead.key == key:
                    nodesHead.value = value
                    return
                nodesHead = nodesHead.next
            newNode = ListNode(key,value,self.nodeList[keyForHash])
            self.nodeList[keyForHash] = newNode

    def get(self, key: int) -> int:
        keyForHash = self.hashKey(key)
        nodesHead = self.nodeList[keyForHash]
        while nodesHead:
            if nodesHead.key == key:
                return nodesHead.value
            nodesHead = nodesHead.next
        return -1

    def remove(self, key: int) -> None:
        keyForHash = self.hashKey(key)
        nodesHead = self.nodeList[keyForHash]
        if nodesHead:
            if nodesHead.key == key:
                nodesHead = nodesHead.next
                self.nodeList[keyForHash] = nodesHead
                return None
            while nodesHead.next:
                if nodesHead.next.key == key:
                    nodesHead.next = nodesHead.next.next
                    return None
                nodesHead = nodesHead.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1))
    print(obj.get(3))
    obj.put(2,1)
    print(obj.get(2))
    obj.remove(2)
    print(obj.get(2))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)