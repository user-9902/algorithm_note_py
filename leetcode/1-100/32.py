"""
32. 最长有效括号
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        栈匹配
        校验一个字符串中括号是否合法，就是用栈处理的。
            遍历s若cur为 ( 存入栈，若为 ) 栈中弹出一个(
            遍历完后，栈为空则s中的括号合法
        这里用同样的方法，筛选出非法的括号的下标
        非法下标中间的就是合法的部分
        """
        # special case
        if not s:
            return 0

        s_len = len(s)

        # 找到那些非法的括号的下标
        stack = []
        for i in range(s_len):
            if stack:
                if s[stack[-1]] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        res = s_len
        if stack:
            res = max(stack[0] - 0, s_len - stack[-1] - 1)
            for i in range(len(stack) - 1):
                res = max(res, stack[i + 1] - stack[i] - 1)
        return res

    def longestValidParentheses2(self, s: str) -> int:
        """
        dp
        遍历字符串s，用一个数组dp存储当前字符串为结尾时，最长的子串
            结尾字符为(：肯定不包含在最长子串中
            结尾字符为): 
                若前一个字符 ( 既 ...() 的情况：
                    dp[i] = 2 + dp[i - 2]
                    dp[i - 2] 表示当前情况是否紧跟在一个合法串后面
                若前一个字符 ) 既 ...)) 的情况：
                    确保字符串是形如 ...((...)) 的合法串
                    dp[i] = dp[i - dp[i - 1] - 2] + dp[i - 1] + 2
                    dp[i - 1] + 2 表示 ...((...)) 中 ((...)) 的长度
                    dp[i - dp[i - 1] - 2] 表示当前情况是否紧跟在一个合法串后面,即 ...((...)) 中 ... 的长度
        """
        s_len= len(s)
        dp = [0] * s_len
        
        max_len = 0
        for i,v in enumerate(s):
            if i > 0 and v == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i > 1 else 0)  + 2
                elif dp[i - 1] > 0 and i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = (dp[i - dp[i - 1] - 2] if i - dp[i - 1] > 1 else 0) + dp[i - 1] + 2
                
                max_len = max(max_len, dp[i])
        return max_len

