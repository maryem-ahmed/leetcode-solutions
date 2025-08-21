# https://leetcode.com/problems/string-to-integer-atoi 
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1
        # to identify sign 
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        #reading data 
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            #check for overflow 
            if res > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            res = res * 10 + digit
            i += 1
        
        #applying sign
        res *= sign
        if res < -2**31:
            return -2**31
        if res > 2**31 - 1:
            return 2**31 - 1
        
        return res
