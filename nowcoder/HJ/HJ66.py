"""
@title:      HJ66 配置文件恢复
@difficulty: 简单
@importance: 3/5
@tags:       业务模拟 
"""

cmds = {
    "reset": "reset what",
    "reset board": "board fault",
    "board add": "where to add",
    "board delete": "no board at all",
    "reboot backplane": "impossible",
    "backplane abort": "install first",
}
cmds_val = [i.split() for i in cmds.keys()]


def output(cmd):
    l = cmd.split()
    res = []
    for i in cmds_val:
        if len(l) != len(i):
            continue
        if all([i[j].startswith(l[j]) for j in range(len(l))]):
            res.append(i)
    return cmds[' '.join(res[0])] if len(res) == 1 else 'unknown command'


while True:
    try:
        cmd = input()
        print(output(cmd))
    except:
        break
