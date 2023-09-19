import unittest

def is_substr(str, sub_str) -> bool:
    s = 0
    for i in range(len(str)):
        if str[i] == sub_str[s] or str[i] == '?':
            s += 1
        else:
            s == 0
        if s == len(sub_str): return i

    return -1


# 贪心 子序列
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
      a = -1
      m = 0
      s = 0
      e = 0
      for i in range(len(p)):
          if p[i] != '*': a = i
          if a != -1 and p[i] == '*': 
              print(s[m:],p[a: i])
              res = is_substr(s[m:],p[a: i])
              if res > -1:
                  a = -1
                  m = res + 1
              else:
                  return False
      return 
  


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isMatch('abcdsa?','a*'), True)



if __name__ == '__main__':
    Solution().isMatch('abcdsa?','a*')