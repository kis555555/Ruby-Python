class Cs :
    count = 0 #루비와는 달리 파이썬에서는 그냥 count로 선언 하면 된다.
    def __init__(self) :
        Cs.count = Cs.count + 1
    @classmethod
    def getCount(cls) :
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()

print(Cs.getCount())