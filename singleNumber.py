class Solution(object):
    def singleNumber(self, nums):
        no_duplicate_list = []
        duplicate_list = []
        tmp = []
        countN = 0
        countD = 0
        for i in nums:
            if i not in no_duplicate_list and i not in duplicate_list:
                no_duplicate_list.append(i)
                countN = countN + 1
            elif i in no_duplicate_list and i not in duplicate_list:
                no_duplicate_list.remove(i)
                duplicate_list.append(i)
                countD = countD + 1
        for _ in range(countN - countD):
            tmp.append(no_duplicate_list.pop())
        return tmp

def main():
    import ast
    nums = ast.literal_eval(input("输入："))
    while True:
        try:
            ret = Solution().singleNumber(nums)
            print(ret)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()