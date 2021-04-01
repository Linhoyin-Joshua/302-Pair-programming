import unittest
import Single_Calculator
import Joint_Calculator

class TestCalc(unittest.TestCase):
    def test_single_calculation(self):
        self.assertEqual(Single_Calculator.single_calculation(100000),0)
        self.assertEqual(Single_Calculator.single_calculation(300000), 9420)
        self.assertEqual(Single_Calculator.single_calculation(1000000), 126500 )
        self.assertEqual(Single_Calculator.single_calculation(3000000), 447300)#447300
        self.assertEqual(Single_Calculator.single_calculation(1234567), 166376)
        self.assertEqual(Single_Calculator.single_calculation(987654321), 148145448)
    def test_joint(self):
        self.assertEqual(Joint_Calculator.joint_calculation(100000,100000),0)
        self.assertEqual(Joint_Calculator.joint_calculation(3000000, 3000000), 894600)
        self.assertEqual(Joint_Calculator.joint_calculation(3144000, 100), 468556)
        self.assertEqual(Joint_Calculator.joint_calculation(1, 2), 0)
        self.assertEqual(Joint_Calculator.joint_calculation(12345678, 87654321),14994599)
        self.assertEqual(Joint_Calculator.joint_calculation(100, 12345678), 1849165)
        self.assertEqual(Joint_Calculator.joint_calculation(50, 3162000), 471607)
        self.assertEqual(Joint_Calculator.joint_calculation(3000000, 144000), 467316)

if __name__ == '__main__':
    unittest.main()
