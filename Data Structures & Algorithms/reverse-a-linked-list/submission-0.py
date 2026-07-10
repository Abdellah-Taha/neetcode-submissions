# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        tmp = head
        arr = []
        while tmp:
            len += 1
            arr.append(tmp.val)
            tmp = tmp.next
        arr = list(reversed(arr))
        tmp = head

        while tmp:
            tmp.val = arr[0]
            arr.pop(0)
            tmp = tmp.next
        return head