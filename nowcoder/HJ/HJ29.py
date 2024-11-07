"""
@title:      HJ29 字符串加解密
@difficulty: 简单
@importance: 3/5
@tags:       凯撒密码
"""

s1 = input()
s2 = input()

"""
💲
str.isalnum 是否都是数字和字母
str.isalpha 是否都是字母
str.isdigit 是否都是数字
str.isupper 是否都是大写
str.islower 是否都是小写
"""


def encode(string: str):
    res = ""
    for c in string:
        if str.isalpha(c):
            if c == "z":
                res += "A"
            elif c == "Z":
                res += "a"
            else:
                res += chr(ord(c) - 31) if str.islower(c) else chr(ord(c) + 33)
        if str.isdigit(c):
            if c == "9":
                res += "0"
            else:
                res += chr(ord(c) + 1)
    return res


def decode(string: str):
    res = ""
    for c in string:
        if str.isalpha(c):
            if c == "A":
                res += "z"
            elif c == "a":
                res += "Z"
            else:
                res += chr(ord(c) - 33) if str.islower(c) else chr(ord(c) + 31)
        if str.isdigit(c):
            if c == "0":
                res += "9"
            else:
                res += chr(ord(c) - 1)
    return res


print(encode(s1))
print(decode(s2))
