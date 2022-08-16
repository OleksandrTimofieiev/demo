print("Hello")
print("Welcome to Telusko")

class NewBlock:

    def __init__(self, stat):
        self.status = stat

    def new_func(self):
        return self.status

block1 = NewBlock("updated")
print(block1.new_func())
