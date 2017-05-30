from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        from random import randint

        num1 = randint(0, 100)

        x = [10, 20, 30]
        y = [[40, 50, 60], [num1, 80, 90]]
        result = solution(x, y)

        self.assertNotEqual(None, result)
        self.assertEqual(result[6], num1)