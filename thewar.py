import sys
import heapq

VEGTELEN = 10**18

def solve():
    bemenet = sys.stdin.read().strip().split()
    poz = 0

    tesztesetek = int(bemenet[poz])
    poz += 1

    kimenetek = []

    for _ in range(tesztesetek):

        csucsok_szama = int(bemenet[poz])
        poz += 1

        ido = []
        for _ in range(csucsok_szama):
            aktualis_sor_szoveges = bemenet[poz: poz + csucsok_szama]
            aktualis_sor = []
            for elem in aktualis_sor_szoveges:
                aktualis_sor.append(int(elem))
            sor = aktualis_sor
            poz += csucsok_szama
            ido.append(sor)

        divyastra_db = int(bemenet[poz])
        poz += 1

        dp = []
        for _ in range(csucsok_szama):
            sor = []
            for _ in range(divyastra_db + 1):
                sor.append(VEGTELEN)
            dp.append(sor)

        dp[0][divyastra_db] = 0

        sor = [(0, 0, divyastra_db)]

        while sor:
            aktualis_ido, aktualis_csucs, maradek_divyastra = heapq.heappop(sor)

            if aktualis_ido != dp[aktualis_csucs][maradek_divyastra]:
                continue

            for kovetkezo_csucs in range(csucsok_szama):
                el_suly = ido[aktualis_csucs][kovetkezo_csucs]

                if kovetkezo_csucs == aktualis_csucs:
                    continue

                uj_ido = aktualis_ido + 2 * el_suly
                if uj_ido < dp[kovetkezo_csucs][maradek_divyastra]:
                    dp[kovetkezo_csucs][maradek_divyastra] = uj_ido
                    heapq.heappush(sor, (uj_ido, kovetkezo_csucs, maradek_divyastra))

                if maradek_divyastra > 0:
                    uj_ido_felezve = aktualis_ido + el_suly
                    if uj_ido_felezve < dp[kovetkezo_csucs][maradek_divyastra - 1]:
                        dp[kovetkezo_csucs][maradek_divyastra - 1] = uj_ido_felezve
                        heapq.heappush(sor, (uj_ido_felezve, kovetkezo_csucs, maradek_divyastra - 1))

        legjobb = min(dp[1])
        valos_ido = legjobb / 2.0

        kimenetek.append(f"{valos_ido:.1f}")

    print("\n".join(kimenetek))


if __name__ == "__main__":
    solve()
