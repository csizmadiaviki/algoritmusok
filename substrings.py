def lcp(a, b):
    hossz = min(len(a), len(b))
    i = 0
    while i < hossz and a[i] == b[i]:
        i += 1
    return i


def kulonbozo_reszstringek(szoveg):
    n = len(szoveg)

    suffixek = []
    for kezdet in range(n):
        vegdarab = szoveg[kezdet:]
        suffixek.append(vegdarab)

    suffixek.sort()

    osszes = n * (n + 1) // 2

    lcp_sum = 0
    for i in range(1, n):
        lcp_sum += lcp(suffixek[i], suffixek[i - 1])

    return osszes - lcp_sum

T = int(input())
for _ in range(T):
    s = input().strip()
    print(kulonbozo_reszstringek(s))
