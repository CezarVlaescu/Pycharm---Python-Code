# class Solution:
#     def mergedlist(self, l1: ListNode, l2: ListNode) -> None:
#         if l1 is None:
#             return l1
#         if l2 is None:
#             return l2
#
#         dummy = ListNode()
#         pointer = dummy
#
#         while l1 and l2:
#             if l1.val < l2.val:
#                 pointer.next = l1
#                 l1 = l1.next
#             else:
#                 pointer.next = l2
#                 l2 = l2.next
#
#             pointer = pointer.next
#
#         if l1:
#             pointer.next = l1
#         else:
#             pointer.next = l2
#
#         return dummy.next
#
#

l = [1, 2, 3]  # define a list
l_iter = iter(l)  # create list_iterator

while True:
    # item will be "end" if iteration is complete
    item = next(l_iter, "end")
    if item == "end":
        break
    print(item)