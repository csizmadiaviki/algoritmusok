import sys
sys.setrecursionlimit(10**7)

def megold_egy_teszt(szobak):
    n = len(szobak)

    dp = []
    for ind in range(n + 1):
        masodik_dim = []
        for ut_inc in range(n + 1):
            harmadik_dim = [-1] * (n + 1)
            masodik_dim.append(harmadik_dim)
        dp.append(masodik_dim)

    def dp_fuggveny(ind, ut_inc, ut_csokk):
        if ind == n:
            return 0

        i_inc = ut_inc + 1
        i_csokk = ut_csokk + 1

        if dp[ind][i_inc][i_csokk] != -1:
            return dp[ind][i_inc][i_csokk]

        aktualis = szobak[ind]

        legjobb = dp_fuggveny(ind + 1, ut_inc, ut_csokk)

        if ut_inc == -1 or aktualis > szobak[ut_inc]:
            kandidat = 1 + dp_fuggveny(ind + 1, ind, ut_csokk)
            if kandidat > legjobb:
                legjobb = kandidat

        if ut_csokk == -1 or aktualis < szobak[ut_csokk]:
            kandidat = 1 + dp_fuggveny(ind + 1, ut_inc, ind)
            if kandidat > legjobb:
                legjobb = kandidat

        dp[ind][i_inc][i_csokk] = legjobb
        return legjobb

    return dp_fuggveny(0, -1, -1)


def main():
    adatok = sys.stdin.read().strip().split()
    if not adatok:
        return

    it = iter(adatok)

    try:
        tesztek_szama = int(next(it))
    except StopIteration:
        return

    eredmenyek = []

    for _ in range(tesztek_szama):
        try:
            n = int(next(it))
        except StopIteration:
            break

        szobak = []
        for _ in range(n):
            try:
                szobak.append(int(next(it)))
            except StopIteration:
                break

        eredmenyek.append(str(megold_egy_teszt(szobak)))

    sys.stdout.write("\n".join(eredmenyek))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
