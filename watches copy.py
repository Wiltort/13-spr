def palindrom():
    #https://contest.yandex.ru/contest/19811/problems/B/
    with open('input.txt') as input:
        s = [a for a in input.readline()]
    l = len(s)
    res=[]
    min = l+1
    
    res = [s[i:i+k] for k in range(2,l+1) for i in range(l-k+1) if s[i:i+k]==list(reversed(s[i:i+k]))]
    if res: 
        return ''.join(sorted(res)[0])
    else:
        return '-1'


if __name__=="__main__":
    print(palindrom())