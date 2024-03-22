import sys

def fib(n, memo):
    if n in memo:
        return memo[n]
    else:
        if n<=1:
            return n
        else:
            memo[n] = fib(n-1, memo)+fib(n-2, memo)
    return memo[n]


def fib_tab(n):
    tab = [-1 for i in range(n)]
    tab[0]=0
    tab[1]=1
    for j in range(2, n):
        tab[j] = tab[j-1]+tab[j-2]
    print(tab)
    return tab[n-1]

print("Calling fibonacci series:")
memo={0:0, 1: 1}
print(fib(int(sys.argv[1]), memo))
print(memo)
print(fib_tab(int(sys.argv[1])))
