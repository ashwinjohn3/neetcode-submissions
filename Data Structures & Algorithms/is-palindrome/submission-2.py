class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        is_palindrome = True
        while i < j:
            left_c = s[i]
            right_c = s[j]
            is_left_alphanumeric = self.is_alpha_numeric(left_c)
            is_right_alphanumeric = self.is_alpha_numeric(right_c)
            if is_left_alphanumeric and is_right_alphanumeric:
                is_palindrome = self.ascii_comparison(left_c, right_c)
                if is_palindrome == False:
                    break
                i += 1
                j -= 1
            elif not is_left_alphanumeric:
                i += 1
            elif not is_right_alphanumeric:
                j -= 1
        return is_palindrome

    def is_numeric(self, c: str) -> bool:
        ascii_val = ord(c)
        return 48 <= ascii_val <= 57

    def is_alpha(self, c: str) -> bool:
        ascii_val = ord(c)
        is_upper = 65 <= ascii_val <= 90
        is_lower = 97 <= ascii_val <= 122
        return is_upper or is_lower
            
    def is_alpha_numeric(self, c: str) -> bool:
        ascii_val = ord(c)
        
        return self.is_numeric(c) or self.is_alpha(c)

    def is_both_alpha_numeric(self, c1, c2) -> bool:
        return (self.is_numeric(c1) and self.is_numeric(c2)) or (self.is_alpha(c1) and self.is_alpha(c2))


    def ascii_comparison(self, c1: str, c2: str) -> bool: 
        print(c1)
        print(c2)
        ascii_diff = abs(ord(c1) - ord(c2))
        is_both_alpha_or_num = self.is_both_alpha_numeric(c1, c2)
        print(ascii_diff)
        return (ascii_diff == 0 or ascii_diff == 32) and is_both_alpha_or_num


        