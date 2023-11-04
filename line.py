def Line():
    #https://contest.yandex.ru/contest/19811/problems/C/
    with open('input.txt') as input:
        n = int(input.readline())
        M = []
        T = False
        for i in range(n):
            X = [int(a) for a in input.readline().split()]
            if X[0] == 0:
                M.append(X[2:4])
            elif X[0] == 1:
                M.append([(X[1]+X[5])/2,(X[2]+X[6])/2])
            #print(M)
            if i == 1 or T:
                A = M[i-1][1]-M[i][1]
                B = M[i][0]-M[i-1][0]
                C = -(A*M[i-1][0]+B*M[i-1][1])
                if A == 0 and B == 0:
                    T = True
                else: 
                    T = False
            elif i > 1:
                if A*M[i][0]+B*M[i][1]+C!=0:
                    return 'No'
    return 'Yes'
        



if __name__=="__main__":
    print(Line())