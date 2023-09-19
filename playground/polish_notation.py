"""
波兰表达式，又称为前缀表达式。
我们常见的运算表达式，都是中缀表达式（运算符位于数字中间），如：1+((2+3)∗4)–5
前缀表达式是指，符号位于数字之前的算数表达式，如：−+1∗+2345
逆波兰表达式，即后缀表达式，运算符置于操作数之后。
对于人来说最直观的是中缀表达式，而前缀表达式（如：-[+1*+234][5] 需要将右边中括号内的内容视为一个整体 ）很不直观。
但对于计算机而言，前缀或后缀表达式却更容易处理。
"""

# 合法数字
DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# 合法符号
SYMBOLS = ('(', ')', '+', '-', '*', '/')
# 符号权重
SYMBOLS_WEIGHT = (1, 1, 2, 2, 3, 3)


def get_weight(str: str):
    # 获取操作符权重的辅助函数
    return SYMBOLS_WEIGHT[SYMBOLS.index(str)]


"""
前后缀表达式的运算的实现如下，这里都是使用栈来实现的，利用了栈的"记忆"功能
"""


def get_calc_result(left: float, right: float, symbol: str):
    # 辅助运算的函数
    match SYMBOLS.index(symbol):
        case 2:
            return left + right
        case 3:
            return left - right
        case 4:
            return left * right
        case 5:
            return left / right


def run_prefix(string: str):
    # 运算前缀表达式，从左向右遍历，连续遍历两个数字，即可进行一次前缀运算。
    sym_stack = []  # 符号的栈
    num_stack = []  # 数字的栈
    counter = 0  # 计数器，表示连续出现数字的次数
    for c in list(string):
        if c in SYMBOLS:
            sym_stack.append(c)
            counter = 0
        elif c in DIGITS:
            # 存在连续连个数字的时候进行运算，并将结果压入栈中；否则直接压入数字栈中
            if counter == 1:
                left = num_stack.pop()
                right = float(c)
                res = get_calc_result(left, right, sym_stack.pop())
                num_stack.append(res)
            else:
                counter += 1
                num_stack.append(float(c))
    # 清空剩余操作符号
    while len(sym_stack) != 0:
        right = num_stack.pop()
        left = num_stack.pop()
        res = get_calc_result(left, right, sym_stack.pop())
        num_stack.append(res)

    return num_stack[0]


def run_postfix(string: str):
    # 运算后缀表达式，从左向右遍历表达式，遇见一个操作符即可进行一次后缀运算。
    # 从代码量上也不难看出，后缀的运算要比前缀简单，只需要一个栈。
    # 当然可以从后向前遍历前缀表达式，来进行优化
    num_stack = []
    for c in list(string):
        if c in DIGITS:
            num_stack.append(float(c))
        if c in SYMBOLS:
            right = num_stack.pop()
            left = num_stack.pop()
            res = get_calc_result(left, right, c)
            num_stack.append(res)

    return num_stack[0]


"""
中缀表达式转前后缀表达式，以下是使用栈实现的：
以中转后为例：
    遇见数字直接置于结果中，因为转化只涉及到符号位置的改变
    遇见操作符
        置于栈（操作符栈）中，待加入至结果中
        若栈中已经存在操作符时，则需比较优先级。
            当前操作符比栈顶的优先级高（需要优先被执行），则压入栈（操作符栈）中。
            当前操作符优先级小于等于栈顶，则出栈（先执行优先级高的操作，既先出栈优先级高的操作）置于结果中。
    遇见'(' 压入栈中，等待 ')'
    遇见')' 清空直至 '(' 的操作符。括号内的内容可以视为子表达式，视为一个整体，遇见')'，则表示遍历完子表达式了。
    
    遍历完成后需清空栈（操作符栈）内剩余的操作符
"""


def exp_checker(str: str) -> bool:
    stack = []
    for s in list(str):
        # 检查字符是否合法
        if s not in LEGAL_CHAR:
            return False
        # 检查括号是否匹配
        if s == '(' or s == ')':
            stack_len = len(stack)
            if stack_len == 0:
                if s == ')':
                    return False
                else:
                    stack.append(s)
            else:
                top = stack.pop()
                if top == s:
                    stack.append(top)
                    stack.append(s)
    return len(stack) == 0


def infix_to_postfix(str: str):
    str_list = list(str)
    # 暂存操作符
    stack = []
    # 后缀结果
    postfix = []
    for c in str_list:
        if c in DIGITS:
            postfix.append(c)
        elif c == '(':
            # 这里可以封装一个函数只考虑无括号的情况，然后拼接即可。
            stack.append(c)
        elif c == ')':
            top = stack.pop()
            while top != '(':
                # 同下方while清空剩余操作符的逻辑。
                postfix.append(top)
                top = stack.pop()
        elif c in SYMBOLS:
            while len(stack) != 0 and get_weight(c) <= get_weight(stack[-1]):
                postfix.append(stack.pop())
            stack.append(c)
    # 清空剩余操作符
    while len(stack) != 0:
        postfix.append(stack.pop())
    # 返回后缀表达式
    return ''.join(postfix)


def infix_to_prevfix(str: str):
    # 中缀转前缀，从后先前遍历中缀即可
    str_list = list(str)

    str_list.reverse()
    stack = []
    postfix = []
    for c in str_list:
        if c in DIGITS:
            postfix.append(c)
        elif c == ')':
            stack.append(c)
        elif c == '(':
            top = stack.pop()
            while top != ')':
                postfix.append(top)
                top = stack.pop()
        elif c in SYMBOLS:
            while len(stack) != 0 and get_weight(c) <= get_weight(stack[-1]):
                postfix.append(stack.pop())
            stack.append(c)

    while len(stack) != 0:
        postfix.append(stack.pop())

    postfix.reverse()
    return ''.join(postfix)


"""
中缀表达式转前后缀表达式，以下是使用二叉树实现的：
构建出一个颗二叉树后，先序遍历即可得到前缀表达式，后续遍历即可得到后缀表达式
构建树的过程常常离不开栈
实际上，下面构建树的实现过程同上方栈的解法，只不过多了些节点构建的过程。
树的解法会更容易理解一些
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class InfixTree:
    def __init__(self, string: str):
        symb_stack = []
        node_stack = []
        for c in list(string):
            node = Node(c)
            if c in DIGITS:
                node_stack.append(node)
            elif c == '(':
                symb_stack.append(node)
            elif c == ')':
                top = symb_stack.pop()
                while top.value != '(':
                    top.right = node_stack.pop()
                    top.left = node_stack.pop()
                    node_stack.append(top)
                    top = symb_stack.pop()
            elif c in SYMBOLS:
                while len(symb_stack) != 0 and get_weight(c) <= get_weight(symb_stack[-1].value):
                    n = symb_stack.pop()
                    n.right = node_stack.pop()
                    n.left = node_stack.pop()
                    node_stack.append(n)
                symb_stack.append(node)

        while len(symb_stack) != 0:
            n = symb_stack.pop()
            n.right = node_stack.pop()
            n.left = node_stack.pop()
            node_stack.append(n)

        self.root = node_stack[0]

    def preorder_traversal(self, node=None):
        # 先序遍历，即可得到后缀表达式
        node = self.root if node == None else node
        if node.left != None:
            self.preorder_traversal(node.left)
        if node.right != None:
            self.preorder_traversal(node.right)
        print(node.value)

    def postorder_traversal(self, node=None):
        # 后续遍历，即可得到前缀表达式，注意顺序是反转的
        node = self.root if node == None else node
        if node.right != None:
            self.postorder_traversal(node.right)
        if node.left != None:
            self.postorder_traversal(node.left)
        print(node.value)
