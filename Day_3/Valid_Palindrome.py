def palindrome(s):
    new_str = s.lower()
    new_s = ""
    
    for i in new_str:
        if i.isalpha() or i.isnumeric():
            new_s += i

    if new_s == new_s[::-1]:
        return True
    return False


print(palindrome("0, P"))