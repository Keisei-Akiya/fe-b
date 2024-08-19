# デフォルトではオーバーロードを行う方法はないらしい．
class Item:
    def __init__(self, qNum):
        self.num = qNum
        self.next = None
    
    def Item(self, qNum, qItem):
        self.num = qNum
        self.next = qItem

def total():
    i1 = Item(100)
    i2 = Item(200, i1)
    i1.next = i2
    return i1.num + i2.num + i1.next.num + i2.next.next.num

total()