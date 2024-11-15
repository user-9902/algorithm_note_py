"""
@title:      HJ95 人民币转换
@difficulty: 中等
@importance: 4/5
@tags:       业务模拟 递归
"""

mp = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖", "拾"]


def cal(num):
    if num < 1:
        return ""
    elif num < 11:
        return mp[num]
    elif num < 20:
        return "拾" + cal(num % 10)
    elif num < 100:
        return cal(num // 10) + "拾" + cal(num % 10)
    elif num < 1000:
        return (
            cal(num // 100)
            + "佰"
            + ("零" if (num % 100) < 10 and num % 100 else "")
            + cal(num % 100)
        )
    elif num < 10000:
        return (
            cal(num // 1000)
            + "仟"
            + ("零" if (num % 1000) < 100 and num % 1000 else "")
            + cal(num % 1000)
        )
    elif num < 100_000_000:
        return cal(num // 10000) + "万" + cal(num % 10000)
    elif 100_000_000 < num:
        return cal(num // 100_000_000) + "亿" + cal(num // 100_000_000)


def cal2(num):
    if num == 0:
        return ''
    elif num < 10:
        return mp[num] + "分"
    else:
        return mp[num // 10] + "角" + cal2(num % 10)


s = [int(i) for i in input().split(".")]
a = "" if s[0] == 0 else (cal(s[0]) + "元")
b = "整" if s[1] == 0 else cal2(s[1])
print("人民币" + a + b)
