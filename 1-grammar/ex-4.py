def funcA():
    if (funcB() > 1):
        ret = "あ"
    elif (funcC()):
        ret = "い"
    else:
        ret = "う"
    return ret

def funcB():
    return 1

def funcC():
    return False

ret = funcA()
print(ret)