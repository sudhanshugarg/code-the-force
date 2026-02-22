# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        race = []
        n = len(lists)
        for i in range(n):
            if lists[i] is not None:
               heapq.heappush(race, Cell(lists[i], i))

        head = None
        curr = None
        while len(race) > 0:
            smallest = heapq.heappop(race)
            if head is None:
                head = smallest.node
                curr = head
            else:
                curr.next = smallest.node
                curr = smallest.node
            if smallest.next is not None:
                heapq.heappush(race, Cell(smallest.next, smallest.id))
        curr.next = None
        return head

class Cell:
    def __init__(self, node: ListNode, id: int):
        self.node = node
        self.id = id

    def __lt__(self, other) -> bool:
        return self.node.val < other.node.val
        
    def __str__(self) -> str:
        return f"[{self.id}: {self.node.val}]"

    def __repr(self) -> str:
        return self.__str__()
