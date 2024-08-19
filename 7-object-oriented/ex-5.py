class Key:
    def __init__(self, qChar):
        self.char = qChar
        self.left = None
    
    def showKey(self):
        left_char = self.left.char if self.left else 'None'
        return f'{self.char}の左隣は{left_char}'

k1 = Key('T')
k2 = Key("Y")
k1.left = k2
k2.left = k1

result = k2.showKey()
print(result)

result = k2.left.showKey()
print(result)