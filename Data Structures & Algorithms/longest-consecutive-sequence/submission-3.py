class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        longest = 0

        for num in store:

            # Start only from the beginning
            if num - 1 not in store:

                length = 1
                curr = num

                while curr + 1 in store:
                    curr += 1
                    length += 1

                longest = max(longest, length)

        return longest