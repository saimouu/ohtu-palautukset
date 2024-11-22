import unittest
from unittest.mock import ANY, Mock

from kauppa import Kauppa
from tuote import Tuote
from varasto import Varasto
from viitegeneraattori import Viitegeneraattori


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        self.varasto_mock.saldo.side_effect = self._varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self._varasto_hae_tuote

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def _varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        if tuote_id == 2:
            return 5
        if tuote_id == 3:
            return 0

    def _varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "leipa", 3)
        if tuote_id == 3:
            return Tuote(3, "juusto", 4)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paaytyttya_pankin_metodia_kutstutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_kahdella_eri_tuotteella_pankin_metodia_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("janne", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("janne", ANY, "54321", ANY, 8)

    def test_kahdella_samalla_tuotteella_pankin_metodia_kutsutaan_oikeilla_arvoilla(
        self,
    ):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("janne", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("janne", ANY, "54321", ANY, 10)

    def test_tuotteella_ja_loppuneella_tuotteella_pankin_metodia_kutsutaan_oikeilla_arvoilla(
        self,
    ):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("janne", "54321")

        self.pankki_mock.tilisiirto.assert_called_with("janne", ANY, "54321", ANY, 5)

    def test_aloita_asiointi_metodi_nollaa_edellisten_ostosten_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("janne", "54321")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "321321")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "321321", ANY, 3)

    def test_uusi_viitenumero_pyydetaan_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called()

    def test_poistettua_tuotetta_ei_makseta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 0)
