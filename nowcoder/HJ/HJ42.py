"""
@title:      HJ42 学英语
@difficulty: 中等
@importance: 3/5
@tags:       业务模拟
@desc:       较 HJ95 更简单
"""

mp = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
]

mp2 = [
    "twen",
    "thir",
    "for",
    "fif",
    "six",
    "seven",
    "eigh",
    "nine",
]


def cal(num):
    if num < 1:
        return ""
    if num < 12:
        return mp[num]
    elif num < 20:
        return mp2[(num % 10) - 2] + "teen"
    elif num < 100:
        res = mp2[(num // 10) - 2] + "ty"
        if num % 10:
            res += " " + cal(num % 10)
        return res
    elif num < 1000:
        res = cal(num // 100) + " hundred"
        if num % 100:
            res += (" and " if num // 10 else " ") + cal(num % 100)
        return res
    elif num < 1_000_000:
        res = cal(num // 1000) + " thousand"
        if num % 1000:
            res += " " + cal(num % 1000)
        return res
    elif num < 1_000_000_000:
        res = cal(num // 1_000_000) + " million"
        if num % 1_000_000:
            res += " " + cal(num % 1_000_000)
        return res


num = int(input())
print(cal(num))
