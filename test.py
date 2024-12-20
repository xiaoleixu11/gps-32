import unittest
import transform


# Docstring para el módulo
"""
Este módulo contiene pruebas unitarias para las funciones de transformación 
de cadenas definidas en el módulo 'transform'.
"""

class TestStringMethods(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para las funciones de transformación
    de cadenas, como convertir a mayúsculas, minúsculas y capitalizar.
    """

    def test_is_upper(self):
        """
        Verifica que la función 'to_upper_case' convierta correctamente 
        una cadena a mayúsculas.
        """
        sting = transform.to_upper_case("hello")
        self.assertEqual(sting, "HELLO")

    def test_is_lower(self):
        """
        Verifica que la función 'to_lower_case' convierta correctamente 
        una cadena a minúsculas.
        """
        sting = transform.to_lower_case("HELLO")
        self.assertEqual(sting, "hello")

    def test_is_capitalize(self):
        """
        Verifica que la función 'to_capitalize' convierta correctamente 
        la primera letra de una cadena a mayúsculas.
        """
        sting = transform.to_capitalize("HELLO")
        self.assertEqual(sting, "Hello")


if __name__ == '__main__':
    unittest.main()

