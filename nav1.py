class Solution:
    def findFinalValue(nums,original):
        def binary(nums,value):
            nums.sort()
            l=0
            r=len(nums)-1

            while l<=r:
                print('help')
                mid=(l+r)//2
                if nums[mid]==value:
                    return True
                elif nums[mid]<value:
                    l=mid+1
                elif nums[mid]>value:
                    r=mid-1
            return False

        while binary(nums,original):
            original=original*2

        return original
print(Solution.findFinalValue([8,19,4,2,15,3],4))