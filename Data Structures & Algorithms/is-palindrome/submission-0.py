class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        first = 0
        last = len(s) - 1
        print(s)
        while first <= last:
            if s[first].lower() != s[last].lower():
                return False
            first = first + 1
            last = last - 1
        return True

        