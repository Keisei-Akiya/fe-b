class Key:
    def __init__(self, qChar):
        self.char = qChar
        self.left = None

k1 = Key("T")
k2 = Key("Y")
k1.left = k2
k2.left = k1
k1.left = k2.left