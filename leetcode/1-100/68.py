"""
68. 文本左右对齐
遍历words，当前word无法塞入前面word组成的行时，生成一行即可。

看到题目第一反应是：text-align: justify; 前端之魂觉醒了[doge]
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)

        left = 0
        right = 0
        s_total = 0
        for i in range(n):
            cur_s = words[i]
            cur_len = len(cur_s)

            if s_total + right - left + cur_len > maxWidth:
                # 生成一行
                space = maxWidth - s_total

                if right - left == 1:
                    words.append(words[left] + ' ' * space)
                else:
                    space_min = space // (right - left - 1)
                    space_rest = space % (right - left - 1)
                    for j in range(left, right - 1):
                        words[j] += ' '*space_min
                        if space_rest:
                            words[j] += ' '
                            space_rest -= 1
                    words.append(''.join(words[left:right]))
                left = i
                right = i + 1
                s_total = cur_len
            else:
                # 还能装下
                s_total += cur_len
                right += 1

        if right <= n:
            for i in range(left, right - 1):
                words[i] += ' '
            words.append(''.join(words[left:n]) + ' ' *
                         (maxWidth - s_total - right + left+1))

        return words[n:]
