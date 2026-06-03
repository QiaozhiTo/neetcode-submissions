class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = collections.defaultdict(int)
        for i in nums:
            count[i]+= 1
        for val in count.values():
            if val > 1:
                return True
        return False
        
        