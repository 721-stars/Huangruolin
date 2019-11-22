import json
import ast

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in nums1:
            if not dic.get(i):
                dic[i] = 1
        new = []
        for i in nums2:
            if dic.get(i):
                new.append(i)
                dic[i] -= 1
        return new


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    line1 = list(ast.literal_eval(input("输入列表1，以逗号隔开：")))
    line2 = list(ast.literal_eval(input("输入列表2，以逗号隔开：")))
    while True:
        try:
            ret = Solution().intersection(line1, line2)
            out = integerListToString(ret)
            print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()