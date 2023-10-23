def play():
    '''
    Принимает на вход массив данных - стоимость акций в день i.
    Вычисляет максимальную выгоду при ограничении не более одной акции в день
    '''
    with open('input.txt') as input:
        n = int(input.readline()) #принимаем массив
        P = [int(a) for a in input.readline().split()]
    S=0
    left = sorted(P)[0:n//2]
    while P:
        max_index, max_value = max(enumerate(P), key=lambda pair: pair[1])
        if max_index == 0:
            P.pop(0)#если максимум на первом месте - удаляем
        else:
            for i in range(max_index-1,-1,-1):
                if P[i] in left:
                    S += max_value-P[i]
                    P.pop(max_index)
                    P.pop(i)
                    break        
    return S

if __name__=="__main__":
    print(play())