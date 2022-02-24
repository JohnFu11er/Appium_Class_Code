import unittest
import pytest

#todo: write this down

class MyTestCase(unittest.TestCase):
    first_option = True
    second_option = False

    @pytest.mark.order(2)
    def test_true(self):
        self.assertTrue(self.first_option, "The variable is set to {}".format(self.first_option))

    @pytest.mark.order(3)
    def test_false(self):
        self.assertFalse(self.second_option, "The variable is set to {}".format(self.second_option))

    @pytest.mark.order(1)
    def test_inequality(self):
        first_string = "value1"
        second_string = "value2"
        self.assertNotEqual(first_string, second_string, f"{first_string} is equal to {second_string}")

    def test_equality(self):
        a = 23
        b = 7
        self.assertEqual(30, a+b)

if __name__ == '__main__':
    unittest.main()
