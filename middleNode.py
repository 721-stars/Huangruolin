class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[int(len(A) / 2)]


def listToListNode(input):
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for i, value in enumerate(input):
        ptr.next = ListNode(value)
        ptr = ptr.next
    return dummyRoot.next


def listNodeToList(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import ast
    lines = ast.literal_eval(input("输入："))
    while True:
        try:
            head = listToListNode(lines)
            ret = Solution().middleNode(head)
            out = listNodeToList(ret)
            print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()