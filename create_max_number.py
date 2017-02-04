class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        z = m + n - k
        ret = list()
        for i in nums1:
        	for j in nums2:
        		m1 = max(nums1[i:i+z])
        		m2 = max(nums[j:j+z])
        		if m1 > m2:
        			