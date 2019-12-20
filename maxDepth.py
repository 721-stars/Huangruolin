class Node(object):
    # 初始化一个节点
    def __init__(self,value = None):
        self.value = value  # 节点值
        self.children = []    # 子节点列表
    # 添加一个孩子节点
    def add_child(self,node):
        self.children.append(node)


# 初始化一颗测试二叉树
def init():
    '''
    初始化一颗测试二叉树:
            1
        3   2   4
       56
    '''
    root = Node('1')
    A = Node('3')
    root.add_child(A)
    root.add_child(Node('2'))
    root.add_child(Node('4'))
    A.add_child(Node('5'))
    A.add_child(Node('6'))
    return root


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1


def main():
    tree = init()
    sol = Solution()
    ans = sol.maxDepth(tree)
    print('N叉树的深度: ', ans)

if __name__ == '__main__':
    main()