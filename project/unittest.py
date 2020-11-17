import unittest
from pro import optimization


class testoptimization(unittest.TestCase):
    def setUp(self):
        self.optimization = optimization(-2, -2, 10000, 0.00089, 0.000001, 0.7)

    def testF2(self):
        self.optimization.f2(-2, -2)

    def testF2g(self):
        self.optimization.f2g(-2, -2)

    def testRosenbrock(self):
        a = self.optimization.rosenbrock_momentum()


if __name__ == '__main__':
    unittest.main()
