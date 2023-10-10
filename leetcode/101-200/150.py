"""
150. 逆波兰表达式求值
计算机计算用的都是后缀表达式
详见 ~/playground/polish_notation.py
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        SYM_DIC = ['-', '+', '*', '/']

        def cal(symbol, left, right):
            left = int(left)
            right = int(right)

            match symbol:
                case '-':
                    return left - right
                case '+':
                    return left + right
                case '*':
                    return left * right
                case '/':
                    return left / right

        num_stack = []
        for i in tokens:
            if i in SYM_DIC:
                right = num_stack.pop()
                left = num_stack.pop()
                num_stack.append(cal(i, left, right))
            else:
                num_stack.append(i)

        return int(num_stack[-1])
