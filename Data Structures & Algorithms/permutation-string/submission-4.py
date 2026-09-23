class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # Build counts for s1 and for the first window in s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        if s1_count == s2_count:
            return True

        # Slide the fixed-size window across s2
        for r in range(len(s1), len(s2)):
            # Add new right character
            s2_count[ord(s2[r]) - ord("a")] += 1

            # Remove old left character
            left_char = s2[r - len(s1)]
            s2_count[ord(left_char) - ord("a")] -= 1

            if s1_count == s2_count:
                return True

        return False