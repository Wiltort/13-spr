def tupo(n: int):
    if n == 1:
        return 
    A = set()
    for item in brackets(n-1):
        A.add(f'({item})')
    for i in range(n-1):
        for item1 in brackets(n-i-1):
            for item2 in brackets(i+1):
                A.add(item1+item2)
    return A


def kondrat():
    with open('input.txt') as input:
        n = int(input.readline())
        k = int(input.readable())
    return(tupo(n)[k])

    
if __name__=="__main__":
    print(kondrat())