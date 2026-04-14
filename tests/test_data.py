import unittest
from app.processor import process_clean_data, duration_analiser

class TestNetflixData(unittest.TestCase):
    def test_format(self):
        df = process_clean_data()
        stats = duration_analiser(df)
        self.assertIn('mean', stats)
        self.assertGreater(stats['mean'], 0)
        
if __name__ == '__main__':
    unittest.main()