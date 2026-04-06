class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Consider only alphanumeric characters and make all chars lower case
        filtered_s = "".join(char.lower() for char in s if char.isalnum())

        # Create array to store chars forward
        forward = []
        for char in filtered_s:
            forward.append(char)

        # Create array to store chars backward
        backward = []
        for i in range(len(filtered_s) - 1, -1, -1):
            backward.append(filtered_s[i])

        # Compare arrays
        if forward == backward:
            return True
        else: 
            return False 