from random import randint

class Bones:
    def __init__(self):
        self.a1 = randint(0,6)
        self.a2 = randint(0,6)

    def __str__(self):
        return f"{self.a1}|{self.a2}"

    def concate(self, other):
        for i in (self.a1,self.a2):
            if other.a1 == i or other.a2 == i:
                return True
        return False


a = Bones()
b = Bones()

print(a,b,sep=' ')

print(a.concate(b))
