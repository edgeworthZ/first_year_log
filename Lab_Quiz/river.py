class Done(Exception): pass

def River(n):
    sum_ = sum([int(x) for x in str(n)])
    return n+sum_

def TryConnectRiver(out,river,N):
    while(N > river):
        river = River(river)
    if(N == river):
        res = (out,N)
        print(*res)
        raise Done

N = int(input('N: '))
one,three,nine = 1,3,9
try:
    while(True):
        TryConnectRiver(1,one,N)
        TryConnectRiver(3,three,N)
        TryConnectRiver(9,nine,N)
        N = River(N)
except Done:
    pass
