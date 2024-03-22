# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head != None:
            a.append(head.val)
            head = head.next
        print(a) #先印出陣列,等一下可以刪掉
        N=len(a)
        for i in range (len(a)):
            if a[i] != a[N-1-i]:return False #頭尾不相同

        return True #先亂寫
