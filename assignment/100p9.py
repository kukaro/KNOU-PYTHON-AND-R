class example:
    def __init__(self, name):
        self.a = 'Hello ' + name + ' !'
        self.b = 'Good-bye ' + name + ' !'


name = 'David'
aaa = example(name)
print(aaa.a)
print(aaa.b)
