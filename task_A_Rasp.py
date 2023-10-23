class Lesson:
    def __init__(self, beg_time, end_time):
        self.beg_time = beg_time
        self.end_time = end_time
    def __str__(self):
        return f'{self.beg_time} {self.end_time}'
    
def raspisanie():
    with open('input.txt') as input:
        n = int(input.readline())
        Lessons = []
        ans = 0
        min = Lesson(0,24)
        Ras = []
        for i in range(n):
            L = Lesson(*[float(a) for a in input.readline().split()])
            Lessons.append(L)
            if L.end_time<min.end_time:
                min = L
                ans = 1
        Ras.append(min)
        Lessons.remove(min)
        Check = True
        while Check:
            min = Lesson(0,24)
            Check = False
            for l in Lessons:
                if l.beg_time>=Ras[-1].end_time and l.end_time<min.end_time:
                    min = l
                    Check = True
            if Check:
                Ras.append(min)
                ans+=1
                Lessons.remove(min)
        print(ans)
        print(*Ras, sep='\n')
        
        
    return 

if __name__=="__main__":
    raspisanie()