import unittest

class ReversePolishCalculator():
    """ A reverse polish calculator """
    def calculate(self, expression):
        symbols = expression.split(" ")
        stack = []  
        for s in symbols:
            if s == '+':
                a = stack.pop()
                b = stack.pop()
                stack.insert(len(stack), a + b) 
            else:
                x = int(s)
                stack.insert(len(stack), x)

        return stack.pop()

class CalculatorTest(unittest.TestCase):

    def test_a_single_number_expression_evaluates_to_the_same_number(self):
        calc = ReversePolishCalculator()
        result = calc.calculate("1")
        self.assertEqual(1, result)
        result = calc.calculate("2")
        self.assertEqual(2, result)

    def test_a_sum_of_two_number_expression(self):
        """ Arrange """
        calc = ReversePolishCalculator()
        
        """ Act """
        result = calc.calculate("10 1 +")

        """ Assert """
        self.assertEqual(11, result)


if __name__ == '__main__':
    unittest.main()
