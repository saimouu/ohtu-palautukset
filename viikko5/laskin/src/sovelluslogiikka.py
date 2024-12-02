class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edellinen_tulos = 0

    def _paivita_edellinen_tulos(self, arvo):
        self._edellinen_tulos = arvo

    def miinus(self, operandi):
        self._paivita_edellinen_tulos(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._paivita_edellinen_tulos(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._paivita_edellinen_tulos(self._arvo)
        self._arvo = 0

    def kumoa(self):
        self._arvo = self._edellinen_tulos
        self._edellinen_tulos = self._arvo

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
