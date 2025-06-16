from typing import Dict, Optional

class Node:
    """
    Linked List Node. Contains key-value pair and links to next and prev elements.
    """
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList:
    """
    Linked List. Represents our history of cached items.
    """
    head: Optional[Node] = None
    tail: Optional[Node] = None


    def add_to_head(self, item: Node):
        """
        Add node to front of list, will have usage for being the most "recent" item.
        """
        if self.head is not None:
            item.next = self.head
            self.head.prev = item

        if self.tail is None:
            self.tail = item

        self.head = item


    def unlink(self, item):
        """
        Remove references from an item, this will be used when reordering history.
        """
        if item is None:
            return

        prev_item = item.prev
        next_item = item.next

        if prev_item is not None:
            prev_item.next = next_item

        if next_item is not None:
            next_item.prev = prev_item

        if self.head == item:
            self.head = next_item

        if self.tail == item:
            self.tail = prev_item

        item.prev = None
        item.next = None


class LRUCache:
    """
    Implements the LRU Cache following spec.
    """
    capacity: int
    cache: Dict[int, Node]
    history: LinkedList


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.history = LinkedList()


    def get(self, key: int) -> int:
        """
        Retrieves value pair of given key, -1 if not found.
        """
        if key not in self.cache:
            return -1

        value_node = self.cache[key]

        if self.history.head != value_node:
            self.history.unlink(value_node)
            self.history.add_to_head(value_node)

        return value_node.value


    def put(self, key: int, value: int) -> None:
        """
        Puts new k-v pair into the cache.
        Replaces value of pair of key already exists.
        If capacity is reached and putting a new pair, we will evict LRU item.
        """
        value_node = Node(key, value)

        if key in self.cache:
            self.remove_item(self.cache[key])

        if len(self.cache) >= self.capacity:
            self.evict_least_recent_item()

        self.history.add_to_head(value_node)
        self.cache[key] = value_node


    def evict_least_recent_item(self):
        """
        Evict LRU Item, found at tail of our linked list.
        """
        last_used = self.history.tail

        if last_used is None:
            return

        self.remove_item(last_used)


    def remove_item(self, item):
        """
        Helper function to remove item represented by node.
        """
        self.history.unlink(item)

        del self.cache[item.key]
        del item


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
