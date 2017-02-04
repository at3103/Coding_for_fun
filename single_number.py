class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = dict()
        s=set()
        for i in nums:
            if d.get(i,0):
                s-={i}
            else:
                d.update({i:1})
                s.add(i)
        return list(s)

S = Solution()
print S.singleNumber([1, 2, 1, 3, 2, 5])