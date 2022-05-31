


"""
Questions to clarify:
thought process:
time complexity:
space complexity:
"""

class ListNode:
    def __init__(self, new_val, next=None):
        self.val = new_val
        self.next = next


class Solution:
    def addTwoNumbers(self):
        ln1 = ListNode(2)
        ln2 = ListNode(4)
        ln3 = ListNode(3)
        ln1.next = ln2
        ln2.next = ln3
        print(ln1.next.val)
        return ""

def main():
    sol = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    sol.addTwoNumbers()

if __name__ == "__main__":
    main()