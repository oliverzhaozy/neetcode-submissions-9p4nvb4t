class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_ptr, end_ptr = 0, len(numbers) - 1

        while numbers[start_ptr] + numbers[end_ptr] != target and start_ptr < end_ptr:
            if numbers[start_ptr] + numbers[end_ptr] > target:
                end_ptr -= 1
            elif numbers[start_ptr] + numbers[end_ptr] < target:
                start_ptr += 1
        
        return [start_ptr + 1, end_ptr + 1]