import methods_to_test
import unittest

class Test(unittest.TestCase):
    #to be run as a test, a method needs to start with 'test'
    def test_method_1(self):
        argument_to_test = 'mano is codin'
        result = methods_to_test.method1(argument_to_test)
        self.assertEqual(result, 'Mano Is Codin')

    def test_method_2(self):
        argument_to_test = 'mano is codin'
        result = methods_to_test.method2(argument_to_test)
        self.assertEqual(result, 'Mano Is Codin')

#needs to be run from terminal with python3 unittesting.py
if __name__ == '__main__':
    unittest.main()