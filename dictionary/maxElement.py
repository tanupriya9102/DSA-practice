class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        s=set(nums)
        dic={}
        for i in s:
            dic[i]=0
        for i in range(len(nums)):
            dic[nums[i]]+=1
        return(max(dic,key=lambda x:dic[x]))
