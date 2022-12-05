class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums=nums1+nums2
        nums.sort()
        # print(nums)
        length=len(nums)
        med=0.0
        if length%2 !=0:
            med=int(length/2)
            return(nums[med])
        else:
            med=int(length/2) 
            return(nums[med]+nums[med-1])/2
