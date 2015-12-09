import unittest
import operator

class ReversePolishCalculator():
    """ A reverse polish calculator """
    def calculate(self, expression):

        # TODO: Use a generator for the parsing of the symbols
        # TODO: Allow to use more than one delimiter and no delimiters at all between operators and operands
        # TODO: Reduce the list of symbols to the expression value.

        symbols = expression.split(" ")
        functions = {
                "+" : operator.add,
                "*" : operator.mul,
                "-" : operator.sub,
                "/" : operator.div
                }
        stack = []  
        for s in symbols:
            if s in functions:
                func = functions[s]
                b = stack.pop()
                a = stack.pop()
                stack.append(func(a, b))
            else:
                x = int(s)
                stack.append(x)

        return stack.pop()

class CalculatorTest(unittest.TestCase):

    def test_a_single_number_expression_evaluates_to_the_same_number(self):
        calc = ReversePolishCalculator()
        result = calc.calculate("1")
        self.assertEqual(1, result)
        result = calc.calculate("2")
        self.assertEqual(2, result)

    def test_a_sum_of_two_numbers_expression(self):
        """ Arrange """
        calc = ReversePolishCalculator()
        
        """ Act """
        result = calc.calculate("10 1 +")

        """ Assert """
        self.assertEqual(11, result)

    def test_a_product_of_two_numbers_expression(self):
        calc = ReversePolishCalculator()
        result = calc.calculate("2 3 *")
        self.assertEqual(6, result)

    def test_a_substraction_of_two_numbers_expression(self):
        calc = ReversePolishCalculator()
        result = calc.calculate("2 1 -")
        self.assertEqual(1, result)
        result = calc.calculate("3 5 -")
        self.assertEqual(-2, result)

    def test_a_division_of_two_numbers_expression(self):
        calc = ReversePolishCalculator()
        result = calc.calculate("4 2 /")
        self.assertEqual(2, result)

if __name__ == '__main__':
    unittest.main()
