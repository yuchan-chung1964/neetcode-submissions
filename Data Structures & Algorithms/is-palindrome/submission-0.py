class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(ch for ch in s if ch.isalnum()).lower()
        for i in range(len(new_str)):
            if new_str[i] != new_str[-i - 1]:
                return False
        return True