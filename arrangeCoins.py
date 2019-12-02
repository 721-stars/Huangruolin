class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解方程 m(m+1) / 2 = n
        l = 0;
        r = n // 2 + 1
        while (l < r):
            m = l + (r - l) // 2
            target = m * (m + 1) / 2
            if target < n - m:
                l = m + 1
            else:
                r = m
        return l


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    line = int(input("输入："))
    while True:
        try:
            ret = Solution().arrangeCoins(line)
            out = intToString(ret)
            print(out)
            break
        except StopIteration:
            break


if __name__ == '__main__':
    main()