import unittest
import return_dataset


class ColumnNamesTest(unittest.TestCase):
 
    def test_add(self):
        c = return_dataset.return_column_names("iris.csv")
        self.assertEqual(c, ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'variety'])
 
 
if __name__ == '__main__':
    unittest.main()