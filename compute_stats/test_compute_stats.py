from unittest import TestCase as TC
from compute_stats import standard_dev, variance, harmonic_mean, maximum, minimum, read_ints, count, summation, average


class TestComputeStats(TC):
    @classmethod
    def setUpClass(self):
        self.data = read_ints('random_nums.txt')

    def test_read_ints(self):
        self.assertEqual(len(self.data), 1000)

    def test_count(self):
        self.assertEqual(count(self.data), 1000)   

    def test_summation(self):     
        self.assertEqual(summation(self.data), 499498)

    def test_average(self):     
        self.assertEqual(average(self.data), 499.498)

    def test_minimum(self):     
        self.assertEqual(minimum(self.data), 1)

    def test_maximum(self):     
        self.assertEqual(maximum(self.data), 997)

    def test_harmonic_mean(self):                        
        self.assertEqual(harmonic_mean(self.data), 129.72817300624072)

    def test_harmonic_mean_on_small_set(self):                        
        self.assertEqual(harmonic_mean([1,4,4]), 2)  

    def test_variance(self):                        
        self.assertAlmostEqual(variance([3, 5, 2, 7, 1, 3]), 3.9166666666)   

    def test_variance_with_data(self):                        
        self.assertAlmostEqual(variance(self.data), 81476.49399, 3)

    def test_standard_dev(self):                        
        self.assertAlmostEqual(standard_dev(self.data), 285.440876, 3)

    def test_standard_dev_on_smaller_set(self):                        
        self.assertAlmostEqual(standard_dev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5]), 2.4, 3)        

