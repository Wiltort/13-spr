def play():
    '''
    Принимает на вход массив данных - стоимость акций в день i.
    Вычисляет максимальную выгоду при ограничении не более одной акции в день
    '''
    with open('input.txt') as input:
        n = int(input.readline()) #принимаем массив
        P = [int(a) for a in input.readline().split()]
    S = 0
    print(P)
    while P:
        if P[0] >= P[1]:
            P.pop(0)#если максимум на первом месте - удаляем
            n -= 1
        else:
            for i in range(2,n):
                if P[i-1]>P[i]:
                    S += P[i-1]-P[0]
                    P = P[i:]
                    n -= i
                    break
            S += P[n-1]-P[0]
            P = []
    return S

if __name__=="__main__":
    print(play())