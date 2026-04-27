class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in numbers:
                j = numbers.index(diff, i + 1)
                return [i + 1, j + 1]