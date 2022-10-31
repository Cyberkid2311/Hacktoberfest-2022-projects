def isPalindrome(num):
    n = num
    rev = 0
    while (num > 0):
        k = num % 10
        rev = (rev * 10) + k
        num = num // 10
    if (n == rev):
        return True
    else:
        return False
 
num = 9687
num = num + 1
while (True):
    if (isPalindrome(num)):
        break
    num = num + 1

print("Next Palindrome :",num)