class Item:
    def __init__(self, qNum):
        self.num = qNum
        self.next = None

i1 = Item(100)

print(i1.num)
print(i1.next)