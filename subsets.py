class Solution:
    def subsets(self, nums):

        result = []

        def backtrack(index, subset):

            if index == len(nums):
                result.append(subset[:])
                return

            # Include current number
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Remove it
            subset.pop()

            # Don't include current number
            backtrack(index + 1, subset)

        backtrack(0, [])

        return result
        
