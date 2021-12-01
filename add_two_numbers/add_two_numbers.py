import sys
from ListNode import ListNode


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    ex:
    ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}
    ListNode{val: 5, next: ListNode{val: 6, next: ListNode{val: 4, next: None}}}
    """
    n1, n2 = [], []
    while l1 is not None:
        n1.append(str(l1.val))
        l1 = l1.next
    while l2 is not None:
        n2.append(str(l2.val))
        l2 = l2.next
    n1.reverse()
    n2.reverse()
    str_digits = list(str(int("".join(n1)) + int("".join(n2))))
    str_digits.reverse()
    i = 0
    head = ListNode(int(str_digits[0]))
    current = head
    while i != len(str_digits) - 1:
        i += 1
        current.next = ListNode(str_digits[i])
        current = current.next
    return head


if __name__ == '__main__':
    """Problem URL: https://leetcode.com/problems/add-two-numbers/ """
    pass