class Calculadora:
    """
    Clase que implementa una calculadora con las cuatro operaciones básicas:
    suma, resta, multiplicación y división.
    """

    def sumar(self, a, b):
        """
        Devuelve la suma de dos números.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de a + b
        """
        return a + b

    def restar(self, a, b):
        """
        Devuelve la resta de dos números.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de a - b
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Devuelve el producto de dos números.
        :param a: Primer número
        :param b: Segundo número
        :return: Resultado de a * b
        """
        return a * b

    def dividir(self, a, b):
        """
        Devuelve la división de dos números.
        Si el divisor es cero se lanza una excepción.
        :param a: Dividendo
        :param b: Divisor
        :return: Resultado de a / b
        :raises ValueError: si b es 0
        """
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
