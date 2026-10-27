class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_lst = sorted(nums)
        
        for i in range(len(sorted_lst) - 1):
            if sorted_lst[i] == sorted_lst[i + 1]:
                return True
        
        return False

# Check if the next number is the same through the array
# True the second one comes up
        