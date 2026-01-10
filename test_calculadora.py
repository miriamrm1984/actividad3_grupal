import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """
    Clase de pruebas unitarias para verificar el correcto funcionamiento
    de la clase Calculadora.
    """

    def setUp(self):
        """
        Se ejecuta antes de cada prueba.
        Crea una nueva instancia de la calculadora.
        """
        self.calc = Calculadora()

    # --- Pruebas de suma ---

    def test_sumar_positivos(self):
        """Comprueba que la suma de dos números positivos es correcta."""
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_sumar_negativos(self):
        """Comprueba que la suma de dos números negativos es correcta."""
        self.assertEqual(self.calc.sumar(-2, -3), -5)

    def test_sumar_con_cero(self):
        """Comprueba que sumar cero no altera el valor."""
        self.assertEqual(self.calc.sumar(0, 5), 5)

    # --- Pruebas de resta ---

    def test_restar_positivos(self):
        """Comprueba la resta entre dos números positivos."""
        self.assertEqual(self.calc.restar(5, 3), 2)

    def test_restar_negativos(self):
        """Comprueba la resta entre dos números negativos."""
        self.assertEqual(self.calc.restar(-5, -3), -2)

    def test_restar_con_cero(self):
        """Comprueba que restar cero no altera el valor."""
        self.assertEqual(self.calc.restar(5, 0), 5)

    # --- Pruebas de multiplicación ---

    def test_multiplicar_positivos(self):
        """Comprueba la multiplicación de dos números positivos."""
        self.assertEqual(self.calc.multiplicar(2, 3), 6)

    def test_multiplicar_negativos(self):
        """Comprueba la multiplicación con un número negativo."""
        self.assertEqual(self.calc.multiplicar(-2, 3), -6)

    def test_multiplicar_con_cero(self):
        """Comprueba que cualquier número multiplicado por cero da cero."""
        self.assertEqual(self.calc.multiplicar(5, 0), 0)

    # --- Pruebas de división ---

    def test_dividir_positivos(self):
        """Comprueba la división exacta entre dos números positivos."""
        self.assertEqual(self.calc.dividir(6, 3), 2)

    def test_dividir_negativos(self):
        """Comprueba la división con resultado negativo."""
        self.assertEqual(self.calc.dividir(-6, 3), -2)

    def test_dividir_decimal(self):
        """Comprueba que la división puede producir decimales."""
        self.assertEqual(self.calc.dividir(5, 2), 2.5)

    def test_dividir_por_cero(self):
        """Comprueba que dividir por cero lanza una excepción."""
        with self.assertRaises(ValueError):
            self.calc.dividir(5, 0)


if __name__ == "__main__":
    unittest.main()
