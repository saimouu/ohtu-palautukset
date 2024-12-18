from luo_peli import luo_peli


def main():
    while True:
        print(
            "Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
        )

        vastaus = input()
        if vastaus:
            tyyppi = vastaus[-1]
        else:
            break

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        peli = luo_peli(tyyppi)

        if peli:
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
