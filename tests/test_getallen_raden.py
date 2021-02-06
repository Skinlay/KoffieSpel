import unittest
from io import StringIO
from unittest.mock import patch
from koffiespel import KoffieSpel

class TestKoffiespel(unittest.TestCase):
    def setUp(self):
        self.koffie = KoffieSpel()

    def test_hebben_we_een_koffiespel_object(self):
        self.assertEqual(type(self.koffie), KoffieSpel)

    def test_kies_nummer(self):
        self.assertGreaterEqual(self.koffie.getal, 1)
        self.assertLessEqual(self.koffie.getal, 100)

    def test_kies_iedere_keer_een_ander_getal(self):
        eerste_getal = self.koffie.getal
        tweede_run = KoffieSpel()
        tweede_getal = tweede_run.getal
        derde_run = KoffieSpel()
        derde_getal = derde_run.getal
        verschil = False
        if eerste_getal != tweede_getal:
            verschil = True
        elif tweede_getal != derde_getal:
            verschil = True
        self.assertTrue(verschil)

    @patch('builtins.input', lambda *args: '10')
    def test_vraag_om_getal(self):
        out = StringIO()
        self.koffie.ask(out=out)
        self.assertEqual(out.getvalue(),"I have a number in mind between 1 and 100, guess which it is: ")
