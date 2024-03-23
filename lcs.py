
def lcs(s1, s2, m, n):
    if m == 0 or n == 0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + lcs(s1, s2, m-1, n-1)
    else:
        return max(lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1))

def solve_recur_dp(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if s1[m-1] == s2[n-1]:
        memo[m][n]=1+solve_recur_dp(s1, s2, m-1, n-1, memo)
    else:
        memo[m][n]=max(solve_recur_dp(s1, s2, m-1, n, memo), solve_recur_dp(s1, s2, m, n-1, memo))
    return memo[m][n]

def lcs_tab(s1, s2, m, n, tab):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2 [j-1]:
                tab[i][j] = 1 + tab[i-1][j-1]
            else:
                tab[i][j] = max(tab[i-1][j], tab[i][j-1])
    return tab

def lcs_memo(s1, s2, m, n):
    def _initialize():
        memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            memo[i][0] = 0
        for j in range(n+1):
            memo[0][j] = 0
        return memo
    # print(memo)
    memo = _initialize()
    solve_recur_dp(s1, s2, m, n, memo)
    print(f"memoization solution : {memo}")
    # print(f"print table : {[print(*line) for line in memo]}")
    print(f"lcs is : {memo[m][n]}")
    memo = _initialize()
    print("*"*50)
    print(lcs_tab(s1, s2, m, n, memo))
    # print([print(*line) for line in memo])

s1 = "bit" # input("Enter first string: ")
s2 = "bat" # input("Enter Second string: ")
# ln = lcs(s1, s2, len(s1), len(s2))
# print(f"lcs of {s1} and {s2} is : {ln}")
lcs_memo(s1, s2, len(s1), len(s2))
