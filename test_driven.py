import unittest
import Single_Calculator
import Joint_Calculator

class TestCalc(unittest.TestCase):
    def test_single_calculation(self):
        self.assertEqual(Single_Calculator.single_calculation(100000),0)# net chargeble income lower than 0
        self.assertEqual(Single_Calculator.single_calculation(170000), 590)#On the first 50000
        self.assertEqual(Single_Calculator.single_calculation(220000), 2620 )# on the second 50000
        self.assertEqual(Single_Calculator.single_calculation(270000), 6450)# on the third 50000
        self.assertEqual(Single_Calculator.single_calculation(320000), 12080)# on the fourth 50000
        self.assertEqual(Single_Calculator.single_calculation(6000000), 897300) # remain
    def test_joint(self):
        self.assertEqual(Joint_Calculator.joint_calculation(100000,100000),0)# net chargeble income lower than 0
        self.assertEqual(Joint_Calculator.joint_calculation(170000, 170000), 1540)#On the first 50000
        self.assertEqual(Joint_Calculator.joint_calculation(220000, 220000), 9560)# on the second 50000
        self.assertEqual(Joint_Calculator.joint_calculation(270000, 270000), 24330)  # on the third 50000
        self.assertEqual(Joint_Calculator.joint_calculation(320000, 320000), 40480)# on the fourth 50000
        self.assertEqual(Joint_Calculator.joint_calculation(6000000, 6000000),1794600)# remain

if __name__ == '__main__':
    unittest.main()
