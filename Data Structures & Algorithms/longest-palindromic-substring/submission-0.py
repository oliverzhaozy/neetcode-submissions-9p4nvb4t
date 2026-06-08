class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create variable to keep track of longest palindrome found thus far
        longest = ""
        max_length = 0

        def helper(left, right):
            nonlocal longest, max_length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Calculate length
                length = right - left + 1

                # Update record if needed
                if length > max_length:
                    max_length = length
                    longest = s[left:right+1]

                # Move left and right pointers
                left -= 1
                right += 1

        # Loop every potential center, starting from index 0
        for i in range(len(s)):
            # At index i, expand outwards
            # Check for both odd and even length palindromes
            helper(i, i)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                helper(i, i + 1)
        return longest