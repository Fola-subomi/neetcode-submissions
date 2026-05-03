class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.casefold()
        s = re.sub(r'[^a-z0-9]', '', s)                
        rev = ''.join(reversed(s))
        if s == rev:
            return True
        else:
            return False
        