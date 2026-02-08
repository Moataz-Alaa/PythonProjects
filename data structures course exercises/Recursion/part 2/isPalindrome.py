
def isPalindrome(strng):
    if strng[0] != strng[len(strng)-1]:
        return False
    if len(strng) in [1, 2]:
        return True
    return isPalindrome(strng[1:len(strng)-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false