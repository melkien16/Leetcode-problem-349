class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersact = []
        for nums in nums1:
            if nums in nums2 and not nums in intersact:
                intersact.append(nums)
        return intersact