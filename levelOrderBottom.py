import json

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []  # 结果列表
        cur = [root]  # 接下来要循环的当前层节点，存的是节点
        while cur:  # 当前层存在结点时
            cur_layer_val = []  # 初始化当前层结果列表为空，存的是val
            next_layer_node = []  # 初始化下一层结点列表为空
            for node in cur:  # 遍历当前层的每一个结点
                if node:  # 如果该结点不为空，则进行记录
                    cur_layer_val.append(node.val)  # 将该结点的值加入当前层结果列表的末尾
                    next_layer_node.extend([node.left, node.right])  # 将该结点的左右孩子结点加入到下一层结点列表
            if cur_layer_val:  # 只要当前层结果列表不为空
                queue.insert(0, cur_layer_val)  # 则把当前层结果列表插入到队列首端
            cur = next_layer_node  # 下一层的结点变成当前层，接着循环
        return queue  # 返回结果队列


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def int2dArrayToString(input):
    return json.dumps(input)


def main():
    line = input("按层序输入树的结点，结点间以逗号隔开：")
    while True:
        try:
            root = stringToTreeNode(line)
            ret = Solution().levelOrderBottom(root)
            out = int2dArrayToString(ret)
            print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()