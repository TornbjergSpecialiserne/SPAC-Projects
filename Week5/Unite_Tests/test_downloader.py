import unittest
from Downloader import *

class test_downloader(unittest.TestCase):
    def setUp(self):
        self.failed_URL = "http://arpeissig.at/wp-content/uploads/2016/02/D7_NHB_ARP_Final_2.pdf"
        self.working_URL = "https://s3-ap-southeast-1.amazonaws.com/aboitizsite-mediafiles/wp-content/uploads/2018/10/12123742/AEV-AR2016_Spread1.pdf"
    
    def test_empty_input(self):
        current_downloader = Downloader()
        result = current_downloader.download("", "")
        self.assertEqual(False, result)

    def test_frist_URL_Right(self):
        current_downloader = Downloader()
        result = current_downloader.download(self.working_URL, "test.pdf")
        self.assertEqual(True, result)

    def test_second_URL_Right(self):
        current_downloader = Downloader()
        result = current_downloader.download("", "test.pdf", self.working_URL)
        self.assertEqual(True, result)

    def test_faild_then_working(self):
        current_downloader = Downloader()
        result = current_downloader.download(self.failed_URL, "test.pdf", self.working_URL)
        self.assertEqual(True, result)

    def test_all_failed_url(self):
        current_downloader = Downloader()
        result = current_downloader.download(self.failed_URL, "test.pdf", self.failed_URL)
        self.assertEqual(False, result)
        
if __name__ == '__main__':
    unittest.main()