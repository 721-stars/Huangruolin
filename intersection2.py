import json
import ast

class Solution(object):
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 保证nums1是最短的，否则交换
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        same_list = []
        for i in nums2:
            if len(nums1) > 0 and i in nums1:
                # 将i进行pop（index只会找到第一个数字为i的下标）
                same_list.append(nums1.pop(nums1.index(i)))
        return same_list

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    line1 = list(ast.literal_eval(input("输入列表1，以逗号隔开：")))
    line2 = list(ast.literal_eval(input("输入列表2，以逗号隔开：")))
    while True:
        try:
            ret = Solution().intersection2(line1, line2)
            out = integerListToString(ret)
            print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()