import unittest
import emailvalidator


class RoteiroTeste(unittest.TestCase):

    def test_ct01(self):
        res = emailvalidator.validate_email("'email'@example.com")
        self.assertEqual(res, 'invalido')

    def test_ct02(self):
        res = emailvalidator.validate_email("email@123.123.123.123")
        self.assertEqual(res, 'invalido')

    def test_ct03(self):
        res = emailvalidator.validate_email("email@example.com")
        self.assertEqual(res, 'valido')

    def test_ct04(self):
        res = emailvalidator.validate_email("1234567890@example.com")
        self.assertEqual(res, 'invalido')

    def test_ct05(self):
        res = emailvalidator.validate_email("firstname+lastname@example.com")
        self.assertEqual(res, 'invalido')

    def test_ct06(self):
        res = emailvalidator.validate_email("_______@example.com")
        self.assertEqual(res, 'invalido')

    def test_ct07(self):
        res = emailvalidator.validate_email("email@example.museum")
        self.assertEqual(res, 'invalido')

    def test_ct08(self):
        res = emailvalidator.validate_email("email@[123.123.123.123]")
        self.assertEqual(res, 'invalido')


class RoteiroTesteEstrutural(unittest.TestCase):

    def test_ct01(self):
        res = emailvalidator.validate_email("_______@example.com")
        self.assertEqual(res, 'invalido')

    def test_ct02(self):
        res = emailvalidator.validate_email("email@example.com")
        self.assertEqual(res, 'valido')

    def test_ct03(self):
        res = emailvalidator.validate_email("email@[123.123.123.123]")
        self.assertEqual(res, 'invalido')

    def test_ct04(self):
        res = emailvalidator.validate_email("firstname+lastname@example.com")
        self.assertEqual(res, 'invalido')


if __name__ == "__main__":
    unittest.main()
