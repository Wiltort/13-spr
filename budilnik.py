def budilnik():
    with open('input.txt') as input:
        N, X, K = [int(a) for a in input.readline().split()]
        B = [int(a) for a in input.readline().split()]
    for i in range(K):
        B = sorted(B)
        Last = B[0]+i*X

    return(sorted(list(T))[K-1])
    
if __name__=="__main__":
    print(budilnik())