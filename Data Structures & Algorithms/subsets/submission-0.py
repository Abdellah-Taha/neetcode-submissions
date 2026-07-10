class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset, sol = [], []

        def backtracking(i):
            if i == n:
                subset.append(sol[:])
                return
            #not chosing i
            backtracking(i+1)

            #chosing i
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
        
        backtracking(0)
        return subset
            
