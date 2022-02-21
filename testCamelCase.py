from unittest import TestCase
import CamelCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('MinaYimam', CamelCase.CamelCase('Mina Yimam'))
        self.assertEqual('', CamelCase.CamelCase(''))
        self.assertEqual('MinaYimam', CamelCase.CamelCase('Mina      YImam   '))
        self.assertEqual('MinaYimam!', CamelCase.CamelCase('Mina   Yimam !'))
        self.assertEqual('Mina', CamelCase.CamelCase('                      Mina'))


