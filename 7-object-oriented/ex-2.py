# Define a class named Key
class Key:
    # Constructor method
    def __init__(self, qChar):
        # Initialize the char attribute with the given qChar argument
        self.char = qChar
        
        # Initialize the left attribute with None(undefined value)
        self.left = None

k1 = Key("A")
print(k1)