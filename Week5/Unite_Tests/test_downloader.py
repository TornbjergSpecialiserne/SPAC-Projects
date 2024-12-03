import unittest
from Downloader import *
from tempfile import NamedTemporaryFile

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
        
    def test_download_and_verify_contents(self):
        # Create a temporary file to store the downloaded content
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file_name = temp_file.name
            
            # Download the file
            downloader = Downloader()
            success = downloader.download(self.working_URL, temp_file_name)
            
            # Check if the download was successful
            self.assertTrue(success)
            
            # Read the contents of the downloaded file
            with open(temp_file_name, 'rb') as file:
                downloaded_content = file.read()
            
            # Download the file again to compare
            response = requests.get(self.working_URL)
            
            # Compare the downloaded content with the original content
            self.assertEqual(downloaded_content, response.content)

        # Clean up the temporary file
        import os
        os.unlink(temp_file_name)

if __name__ == '__main__':
    unittest.main()