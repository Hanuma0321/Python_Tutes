class Phonbook:
    def add(a,b):
        return a+b
    def __init__(self):
        self.numbers = {}
    def add(self,name,number):
        self.numbers[name] = number
    def lookup(self,name):
        return self.numbers[name]
