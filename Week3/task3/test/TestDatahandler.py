import unittest
from  csv_data_handler import *

class TestDataHandler(unittest.TestCase):

    def test_should_return_file_not_found_error(self):
        data_handler = CSVDatahandler()
        error = data_handler.open_file("Wrong")
        self.assertEqual(error,"file not found")

    def test_should_read_data(self):
        data_handler = CSVDatahandler()
        error = data_handler.open_file(".\\test\\TestData")
        self.assertEqual(error,"file loaded")
        data = next(data_handler.get_data())
        self.assertEqual(data[0],"file read and data got")
        data_handler.close_file()

if __name__ == "__main__":
    unittest.main()
