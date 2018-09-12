class Animal:
    x = 0
    def __init__(self):
        print("LOLKA")
    def party(self):
        self.x+=1
        print('value of x', self.x)
        return self.x
    def __del__(self):
        print('I am dead')
an = Animal()
an.party()
print(an.party())
