def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome('aba'))
print(is_palindrome('abca'))
print(is_palindrome('abba'))