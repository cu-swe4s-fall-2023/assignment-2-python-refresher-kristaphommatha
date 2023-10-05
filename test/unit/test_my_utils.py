import sys
import my_utils
import unittest
import random
import os


class TestMyUtils(unittest.TestCase):

    def test_mean_positive(self):
        nums = []
        for i in range(10000):
            nums.append(random.randint(1, 100))

        self.assertAlmostEqual(my_utils.get_mean(nums), 50, delta=1.5)

    def test_mean_negative(self):
        negCase = []
        self.assertEqual(None, my_utils.get_mean(nums))

    def test_med_positive(self):
        nums = []
        for i in range(10000):
            nums.append(random.randint(1, 100))
        self.assertAlmostEqual(my_utils.get_median(nums), 50, delta=1.5)

    def test_mean_negative(self):
        negCase = []
        self.assertEqual(None, my_utils.get_median(negCase))

    def test_stdev_positive(self):
        nums = []
        for i in range(10000):
            nums.append(random.randint(1, 100))
        self.assertAlmostEqual(my_utils.get_stdev(nums), 28.57, delta=1)

    def test_stdev_negative(self):
        negCase = []
        self.assertEqual(None, my_utils.get_median(negCase))


if __name__ == "__main__":
    unittest.main()
