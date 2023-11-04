from string import ascii_lowercase as alc

class CharAnalise():
    def __init__(self):
        self.dict = {c:0 for c in alc}
    
    def analise(self, s: str):
        for c in s:
            self.dict[c] += 1
        return self.dict


def pp():
    with open('input.txt') as input:
        s = input.readline().rstrip()
        t = input.readline()
    a1 = CharAnalise()
    #print(a1.dict)
    a1.analise(s)
    #print(a1.dict)
    a2 = CharAnalise()
    a2.analise(t)
    for c in alc:
        if a1.dict[c]>a2.dict[c]:
            return False
    return True

    
if __name__=="__main__":
    print(pp())