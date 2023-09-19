"""
126. 单词接龙 II
图; bfs; dfs; 回溯
这题属于图的数据结构
    每个字符都是一个顶点
    相差一个字符的两个字符之间有一条边
题意也可抽象为求图中一个点至另一个点的最短路径
"""
@todo

from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        pass

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        dfs
        剪枝效果差
        这里是寻找最短转化路径，显然应该使用bfs来实现
        """
        if endWord not in wordList:
            return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        b_index = wordList.index(beginWord)
        e_index = wordList.index(endWord)

        n = len(wordList)
        m = len(wordList[0])
        map = [[] for _ in range(n)]

        # n^2
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(m):
                    if count > 1:
                        break
                    if wordList[i][k] != wordList[j][k]:
                        count += 1
                if count == 1:
                    map[i].append(j)
                    map[j].append(i)

        res = []
        r = []

        def dfs(index):
            for i in map[index]:
                # 剪枝 得不到更优解了
                if res and len(r) > len(res[0]):
                    break

                if i in r:
                    continue

                if i == e_index:
                    # 得到更优解 清空非最优
                    if res and len(res[0]) > len(r):
                        res.clear()
                    res.append(r[:])
                    continue
                r.append(i)
                dfs(i)
                # 回溯
                r.pop()

        dfs(b_index)

        for i in res:
            for j in range(len(i)):
                i[j] = wordList[i[j]]
            i.append(endWord)
            i.insert(0, beginWord)

        return res

    def findLadders3(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        bfs
        广度优先遍历
        如：能从 1 跳到 [2, 3] 那么后续就无需再次遍历 2 和 3，从1 -> 1 -> 3 是最快的路径
        """
        if endWord not in wordList:
            return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        b_index = wordList.index(beginWord)
        e_index = wordList.index(endWord)

        n = len(wordList)
        m = len(wordList[0])


        # n^2
        map = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(m):
                    if count > 1:
                        break
                    if wordList[i][k] != wordList[j][k]:
                        count += 1
                if count == 1:
                    map[i].append(j)
                    map[j].append(i)
        # 广度优先遍历利用队列
        queue = [(0, None, b_index)]  # (当前深度，父节点，map index)
        record = [False] * n  # 当前下标是否遍历到了

        # 当前层的左右边界[l,r)
        l = 0
        r = 1

        res = []
        while r - l > 0:
            # 清空当前层的可能性
            for i in range(l, r):
                record[queue[i][2]] = True

            # 添加下一层
            cnt = 0  # 下一层的个数
            for x in range(l, r):
                cur = queue[x]

                for y in map[cur[2]]:
                    if record[y]:
                        continue

                    child = (cur[0] + 1, cur, y)
                    if y == e_index:
                        res.append(child)
                    else:
                        cnt += 1
                        queue.append(child)
            if res:
                break
            l = r
            r += cnt

        # 翻译出结果
        ans = []
        for i in res:
            a = []
            cur = i
            while cur:
                a.insert(0, wordList[cur[2]])
                cur = cur[1]
            ans.append(a)
        return ans


rrr = ["aaaaa","caaaa","cbaaa","daaaa","dbaaa","eaaaa","ebaaa","faaaa","fbaaa","gaaaa","gbaaa","haaaa","hbaaa","iaaaa","ibaaa","jaaaa","jbaaa","kaaaa","kbaaa","laaaa","lbaaa","maaaa","mbaaa","naaaa","nbaaa","oaaaa","obaaa","paaaa","pbaaa","bbaaa","bbcaa","bbcba","bbdaa","bbdba","bbeaa","bbeba","bbfaa","bbfba","bbgaa","bbgba","bbhaa","bbhba","bbiaa","bbiba","bbjaa","bbjba","bbkaa","bbkba","bblaa","bblba","bbmaa","bbmba","bbnaa","bbnba","bboaa","bboba","bbpaa","bbpba","bbbba","abbba","acbba","dbbba","dcbba","ebbba","ecbba","fbbba","fcbba","gbbba","gcbba","hbbba","hcbba","ibbba","icbba","jbbba","jcbba","kbbba","kcbba","lbbba","lcbba","mbbba","mcbba","nbbba","ncbba","obbba","ocbba","pbbba","pcbba","ccbba","ccaba","ccaca","ccdba","ccdca","cceba","cceca","ccfba","ccfca","ccgba","ccgca","cchba","cchca","cciba","ccica","ccjba","ccjca","cckba","cckca","cclba","cclca","ccmba","ccmca","ccnba","ccnca","ccoba","ccoca","ccpba","ccpca","cccca","accca","adcca","bccca","bdcca","eccca","edcca","fccca","fdcca","gccca","gdcca","hccca","hdcca","iccca","idcca","jccca","jdcca","kccca","kdcca","lccca","ldcca","mccca","mdcca","nccca","ndcca","occca","odcca","pccca","pdcca","ddcca","ddaca","ddada","ddbca","ddbda","ddeca","ddeda","ddfca","ddfda","ddgca","ddgda","ddhca","ddhda","ddica","ddida","ddjca","ddjda","ddkca","ddkda","ddlca","ddlda","ddmca","ddmda","ddnca","ddnda","ddoca","ddoda","ddpca","ddpda","dddda","addda","aedda","bddda","bedda","cddda","cedda","fddda","fedda","gddda","gedda","hddda","hedda","iddda","iedda","jddda","jedda","kddda","kedda","lddda","ledda","mddda","medda","nddda","nedda","oddda","oedda","pddda","pedda","eedda","eeada","eeaea","eebda","eebea","eecda","eecea","eefda","eefea","eegda","eegea","eehda","eehea","eeida","eeiea","eejda","eejea","eekda","eekea","eelda","eelea","eemda","eemea","eenda","eenea","eeoda","eeoea","eepda","eepea","eeeea","ggggg","agggg","ahggg","bgggg","bhggg","cgggg","chggg","dgggg","dhggg","egggg","ehggg","fgggg","fhggg","igggg","ihggg","jgggg","jhggg","kgggg","khggg","lgggg","lhggg","mgggg","mhggg","ngggg","nhggg","ogggg","ohggg","pgggg","phggg","hhggg","hhagg","hhahg","hhbgg","hhbhg","hhcgg","hhchg","hhdgg","hhdhg","hhegg","hhehg","hhfgg","hhfhg","hhigg","hhihg","hhjgg","hhjhg","hhkgg","hhkhg","hhlgg","hhlhg","hhmgg","hhmhg","hhngg","hhnhg","hhogg","hhohg","hhpgg","hhphg","hhhhg","ahhhg","aihhg","bhhhg","bihhg","chhhg","cihhg","dhhhg","dihhg","ehhhg","eihhg","fhhhg","fihhg","ghhhg","gihhg","jhhhg","jihhg","khhhg","kihhg","lhhhg","lihhg","mhhhg","mihhg","nhhhg","nihhg","ohhhg","oihhg","phhhg","pihhg","iihhg","iiahg","iiaig","iibhg","iibig","iichg","iicig","iidhg","iidig","iiehg","iieig","iifhg","iifig","iighg","iigig","iijhg","iijig","iikhg","iikig","iilhg","iilig","iimhg","iimig","iinhg","iinig","iiohg","iioig","iiphg","iipig","iiiig","aiiig","ajiig","biiig","bjiig","ciiig","cjiig","diiig","djiig","eiiig","ejiig","fiiig","fjiig","giiig","gjiig","hiiig","hjiig","kiiig","kjiig","liiig","ljiig","miiig","mjiig","niiig","njiig","oiiig","ojiig","piiig","pjiig","jjiig","jjaig","jjajg","jjbig","jjbjg","jjcig","jjcjg","jjdig","jjdjg","jjeig","jjejg","jjfig","jjfjg","jjgig","jjgjg","jjhig","jjhjg","jjkig","jjkjg","jjlig","jjljg","jjmig","jjmjg","jjnig","jjnjg","jjoig","jjojg","jjpig","jjpjg","jjjjg","ajjjg","akjjg","bjjjg","bkjjg","cjjjg","ckjjg","djjjg","dkjjg","ejjjg","ekjjg","fjjjg","fkjjg","gjjjg","gkjjg","hjjjg","hkjjg","ijjjg","ikjjg","ljjjg","lkjjg","mjjjg","mkjjg","njjjg","nkjjg","ojjjg","okjjg","pjjjg","pkjjg","kkjjg","kkajg","kkakg","kkbjg","kkbkg","kkcjg","kkckg","kkdjg","kkdkg","kkejg","kkekg","kkfjg","kkfkg","kkgjg","kkgkg","kkhjg","kkhkg","kkijg","kkikg","kkljg","kklkg","kkmjg","kkmkg","kknjg","kknkg","kkojg","kkokg","kkpjg","kkpkg","kkkkg","ggggx","gggxx","ggxxx","gxxxx","xxxxx","xxxxy","xxxyy","xxyyy","xyyyy","yyyyy","yyyyw","yyyww","yywww","ywwww","wwwww","wwvww","wvvww","vvvww","vvvwz","avvwz","aavwz","aaawz","aaaaz"]

test1 = ["aaaaa", "ggggg", rrr]
test2 = ["hit", "cog", ["hot","dot","dog","lot","log","cog"]]

Solution().findLadders3(*test2)
