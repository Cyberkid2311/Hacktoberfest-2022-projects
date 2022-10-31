def check_equal(str1, str2):
    res = ""
    str1 = str1+str1
    if(str1.count(str2) >0):
        res = "Same"
    else:
        res = "Not Same"
    return res

str1 = "abcde"
str2 = "bcdea"
print(check_equal(str1,str2))