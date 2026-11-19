import unittest
from logica import comparar, generar_numero

class PruebasLogica(unittest.TestCase):
    def test_comparar(self):
        self.assertEqual(comparar(5, 5), "correcto")
        self.assertEqual(comparar(3, 5), "mayor")
        self.assertEqual(comparar(8, 5), "menor")

    def test_generar_en_rango(self):
        for _ in range(100):
            self.assertTrue(1 <= generar_numero(1, 10) <= 10)

if __name__ == "__main__":
    unittest.main()